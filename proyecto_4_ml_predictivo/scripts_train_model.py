"""Entrena modelos de churn y guarda el mejor junto con métricas y visualizaciones."""
import json
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_auc_score, classification_report, RocCurveDisplay
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

def main():
    root = Path(__file__).resolve().parent
    data_path = root / 'data' / 'customer_churn.csv'
    df = pd.read_csv(data_path)

    X = df.drop(columns=['churn'])
    y = df['churn']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, stratify=y, random_state=42)

    models = {
        'logistic_regression': Pipeline([
            ('scaler', StandardScaler()),
            ('model', LogisticRegression(max_iter=1000, random_state=42))
        ]),
        'random_forest': RandomForestClassifier(n_estimators=300, random_state=42, class_weight='balanced')
    }

    results = {}
    best_name, best_model, best_auc = None, None, -1

    for name, model in models.items():
        model.fit(X_train, y_train)
        proba = model.predict_proba(X_test)[:, 1]
        preds = model.predict(X_test)
        auc = roc_auc_score(y_test, proba)
        report = classification_report(y_test, preds, output_dict=True)
        results[name] = {'roc_auc': auc, 'report': report}

        if auc > best_auc:
            best_auc = auc
            best_name = name
            best_model = model

    models_dir = root / 'models'
    viz_dir = root / 'visualizations'
    models_dir.mkdir(exist_ok=True)
    viz_dir.mkdir(exist_ok=True)

    joblib.dump(best_model, models_dir / 'churn_model.pkl')

    # ROC curve del mejor
    proba_best = best_model.predict_proba(X_test)[:, 1]
    RocCurveDisplay.from_predictions(y_test, proba_best)
    plt.title(f'Curva ROC - {best_name}')
    plt.tight_layout()
    plt.savefig(viz_dir / 'roc_curve.png', dpi=140)
    plt.close()

    # Feature importance
    if best_name == 'random_forest':
        importances = pd.Series(best_model.feature_importances_, index=X.columns).sort_values(ascending=False)
    else:
        coefs = best_model.named_steps['model'].coef_[0]
        importances = pd.Series(abs(coefs), index=X.columns).sort_values(ascending=False)

    plt.figure(figsize=(8,4))
    importances.head(10).plot(kind='bar')
    plt.title('Top 10 variables más relevantes')
    plt.tight_layout()
    plt.savefig(viz_dir / 'feature_importance.png', dpi=140)
    plt.close()

    metrics_path = models_dir / 'metrics.json'
    with open(metrics_path, 'w', encoding='utf-8') as f:
        json.dump({'best_model': best_name, 'results': results}, f, ensure_ascii=False, indent=2)

    print(f'Modelo entrenado: {best_name} (ROC-AUC={best_auc:.4f})')

if __name__ == '__main__':
    main()
