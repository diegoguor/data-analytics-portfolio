"""Ejecuta predicción de churn para un archivo CSV de entrada."""
import argparse
import joblib
import pandas as pd
from pathlib import Path

def main(input_csv: str, output_csv: str):
    root = Path(__file__).resolve().parent
    model = joblib.load(root / 'models' / 'churn_model.pkl')
    df = pd.read_csv(input_csv)
    features = df.drop(columns=['churn'], errors='ignore')
    proba = model.predict_proba(features)[:, 1]
    pred = (proba >= 0.5).astype(int)

    out_df = df.copy()
    out_df['probabilidad_churn'] = proba
    out_df['prediccion_churn'] = pred
    out_df.to_csv(output_csv, index=False)
    print('Predicciones generadas en', output_csv)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='Ruta CSV de entrada')
    parser.add_argument('--output', required=True, help='Ruta CSV de salida')
    args = parser.parse_args()
    main(args.input, args.output)
