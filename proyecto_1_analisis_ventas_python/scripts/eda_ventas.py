"""EDA de ventas con generación de KPIs y visualizaciones."""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

def main():
    root = Path(__file__).resolve().parents[1]
    df = pd.read_csv(root / 'data' / 'sales_ecommerce.csv', parse_dates=['date'])

    # Limpieza básica
    df = df.drop_duplicates(subset=['order_id'])
    df = df[df['net_sales'] >= 0]

    # KPIs
    kpis = {
        'total_ventas_netas': float(df['net_sales'].sum()),
        'total_ordenes': int(df['order_id'].nunique()),
        'ticket_promedio': float(df['net_sales'].mean()),
        'margen_promedio_pct': float((df['profit'].sum() / df['net_sales'].sum()) * 100),
        'tasa_devolucion_pct': float(df['is_returned'].mean() * 100)
    }
    kpis_df = pd.DataFrame([kpis])
    kpis_df.to_csv(root / 'data' / 'kpis_resumen.csv', index=False)

    viz = root / 'visualizations'
    viz.mkdir(exist_ok=True)

    sns.set_theme(style='whitegrid')

    # Ventas mensuales
    mensual = df.set_index('date').resample('ME')['net_sales'].sum().reset_index()
    plt.figure(figsize=(10,4))
    sns.lineplot(data=mensual, x='date', y='net_sales', marker='o')
    plt.title('Ventas netas mensuales')
    plt.xlabel('Mes')
    plt.ylabel('Ventas netas')
    plt.tight_layout()
    plt.savefig(viz / 'ventas_mensuales.png', dpi=140)
    plt.close()

    # Top categorías
    cat = df.groupby('category', as_index=False)['net_sales'].sum().sort_values('net_sales', ascending=False)
    plt.figure(figsize=(8,4))
    sns.barplot(data=cat, x='category', y='net_sales', hue='category', palette='viridis', legend=False)
    plt.title('Ventas netas por categoría')
    plt.xlabel('Categoría')
    plt.ylabel('Ventas netas')
    plt.tight_layout()
    plt.savefig(viz / 'ventas_categoria.png', dpi=140)
    plt.close()

    # Devoluciones por región
    ret = df.groupby('region', as_index=False)['is_returned'].mean()
    ret['is_returned'] = ret['is_returned'] * 100
    plt.figure(figsize=(8,4))
    sns.barplot(data=ret, x='region', y='is_returned', hue='region', palette='magma', legend=False)
    plt.title('Tasa de devolución por región (%)')
    plt.xlabel('Región')
    plt.ylabel('% Devolución')
    plt.tight_layout()
    plt.savefig(viz / 'devoluciones_region.png', dpi=140)
    plt.close()

    # Correlación numérica
    plt.figure(figsize=(7,5))
    corr = df[['quantity','unit_price','discount_pct','net_sales','cost','profit']].corr(numeric_only=True)
    sns.heatmap(corr, annot=True, cmap='Blues', fmt='.2f')
    plt.title('Mapa de correlación')
    plt.tight_layout()
    plt.savefig(viz / 'heatmap_correlacion.png', dpi=140)
    plt.close()

    print('EDA completado. KPIs y visualizaciones generados.')

if __name__ == '__main__':
    main()
