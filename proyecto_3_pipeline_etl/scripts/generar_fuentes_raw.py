"""Genera fuentes RAW sintéticas para pipeline ETL."""
import numpy as np
import pandas as pd
from pathlib import Path

np.random.seed(7)

def main():
    root = Path(__file__).resolve().parents[1]
    raw = root / 'data' / 'raw'
    raw.mkdir(parents=True, exist_ok=True)

    n_clientes = 1200
    clientes = pd.DataFrame({
        'cliente_id': range(1, n_clientes+1),
        'ciudad': np.random.choice(['Bogotá','Medellín','Cali','Barranquilla','Bucaramanga'], n_clientes),
        'segmento': np.random.choice(['SMB','Mid-Market','Enterprise'], n_clientes, p=[0.55,0.30,0.15]),
        'fecha_registro': pd.to_datetime(np.random.choice(pd.date_range('2022-01-01','2025-06-30'), n_clientes))
    })

    n_ordenes = 6500
    ordenes = pd.DataFrame({
        'orden_id': [f'O{i:06d}' for i in range(1, n_ordenes+1)],
        'cliente_id': np.random.randint(1, n_clientes+1, n_ordenes),
        'fecha_orden': pd.to_datetime(np.random.choice(pd.date_range('2024-01-01','2025-12-31'), n_ordenes)),
        'canal': np.random.choice(['Online','Fuerza Comercial','Partners'], n_ordenes, p=[0.5,0.35,0.15]),
        'monto_orden': np.round(np.random.gamma(shape=4, scale=120, size=n_ordenes), 2)
    })

    pagos = ordenes[['orden_id']].copy()
    pagos['metodo_pago'] = np.random.choice(['Tarjeta','Transferencia','PSE','Efectivo'], n_ordenes, p=[0.45,0.25,0.2,0.1])
    pagos['estado_pago'] = np.random.choice(['Pagado','Pendiente','Rechazado'], n_ordenes, p=[0.9,0.08,0.02])
    pagos['fecha_pago'] = ordenes['fecha_orden'] + pd.to_timedelta(np.random.randint(0,10,n_ordenes), unit='D')

    # Inyectar algunos valores nulos para simular calidad
    ordenes.loc[ordenes.sample(frac=0.01, random_state=1).index, 'monto_orden'] = np.nan

    clientes.to_csv(raw / 'clientes.csv', index=False)
    ordenes.to_csv(raw / 'ordenes.csv', index=False)
    pagos.to_csv(raw / 'pagos.csv', index=False)

    print('Fuentes RAW generadas en', raw)

if __name__ == '__main__':
    main()
