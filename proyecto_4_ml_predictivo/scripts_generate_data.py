"""Genera dataset sintético para churn prediction."""
from sklearn.datasets import make_classification
import pandas as pd
from pathlib import Path

def main():
    root = Path(__file__).resolve().parent
    X, y = make_classification(
        n_samples=3500,
        n_features=12,
        n_informative=8,
        n_redundant=2,
        n_classes=2,
        weights=[0.72, 0.28],
        random_state=42
    )

    cols = [
        'uso_servicio_mensual','soportes_tickets','antiguedad_meses','satisfaccion',
        'consumo_promedio','retrasos_pago','ingreso_estimado','interacciones_app',
        'descuentos_recibidos','uso_canales_digitales','nps','variabilidad_consumo'
    ]

    df = pd.DataFrame(X, columns=cols)
    # Escalar algunas columnas para mayor realismo
    df['antiguedad_meses'] = (df['antiguedad_meses'].abs() * 12).round(0)
    df['satisfaccion'] = (3 + df['satisfaccion']).clip(1, 5).round(2)
    df['retrasos_pago'] = (df['retrasos_pago'].abs() * 2).round(0)
    df['ingreso_estimado'] = (2500 + (df['ingreso_estimado'] * 800)).clip(800, 12000).round(2)
    df['churn'] = y

    out = root / 'data' / 'customer_churn.csv'
    out.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(out, index=False)
    print('Dataset churn creado en', out)

if __name__ == '__main__':
    main()
