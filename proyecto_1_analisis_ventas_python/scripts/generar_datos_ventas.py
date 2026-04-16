"""Genera dataset sintético de ventas e-commerce y base SQLite para análisis."""
import numpy as np
import pandas as pd
import sqlite3
from pathlib import Path

np.random.seed(42)

def generar_datos(n=5000):
    fechas = pd.date_range('2023-01-01', '2025-12-31', freq='D')
    categorias = ['Tecnología', 'Hogar', 'Moda', 'Deportes', 'Belleza']
    regiones = ['Bogotá', 'Antioquia', 'Valle', 'Costa', 'Centro']
    canales = ['Web', 'App', 'Marketplace']

    df = pd.DataFrame({
        'order_id': [f'ORD{100000+i}' for i in range(n)],
        'date': np.random.choice(fechas, n),
        'customer_id': np.random.randint(1000, 4000, n),
        'category': np.random.choice(categorias, n, p=[0.28,0.22,0.2,0.18,0.12]),
        'region': np.random.choice(regiones, n),
        'channel': np.random.choice(canales, n, p=[0.5,0.35,0.15]),
        'quantity': np.random.randint(1, 7, n),
        'unit_price': np.round(np.random.uniform(20, 500, n), 2),
        'discount_pct': np.round(np.random.choice([0, 5, 10, 15, 20], n, p=[0.35,0.25,0.2,0.15,0.05]), 2),
        'is_returned': np.random.choice([0,1], n, p=[0.93,0.07])
    })

    df['gross_sales'] = np.round(df['quantity'] * df['unit_price'], 2)
    df['discount_value'] = np.round(df['gross_sales'] * (df['discount_pct']/100), 2)
    df['net_sales'] = np.round(df['gross_sales'] - df['discount_value'], 2)
    df['cost'] = np.round(df['net_sales'] * np.random.uniform(0.55, 0.82, n), 2)
    df['profit'] = np.round(df['net_sales'] - df['cost'], 2)
    return df

def main():
    root = Path(__file__).resolve().parents[1]
    data_path = root / 'data' / 'sales_ecommerce.csv'
    db_path = root / 'data' / 'sales_ecommerce.db'
    df = generar_datos()
    df.to_csv(data_path, index=False)

    conn = sqlite3.connect(db_path)
    df.to_sql('sales', conn, if_exists='replace', index=False)
    conn.close()

    print(f'Dataset creado: {data_path}')
    print(f'Base SQLite creada: {db_path}')

if __name__ == '__main__':
    main()
