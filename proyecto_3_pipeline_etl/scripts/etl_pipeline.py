"""Pipeline ETL para consolidar clientes, órdenes y pagos."""
import json
import pandas as pd
from pathlib import Path

def validar(df, nombre):
    return {
        'tabla': nombre,
        'filas': int(len(df)),
        'columnas': int(df.shape[1]),
        'nulos_por_columna': {k:int(v) for k,v in df.isna().sum().to_dict().items()},
        'duplicados': int(df.duplicated().sum())
    }

def main():
    root = Path(__file__).resolve().parents[1]
    raw = root / 'data' / 'raw'
    processed = root / 'data' / 'processed'
    processed.mkdir(parents=True, exist_ok=True)

    clientes = pd.read_csv(raw / 'clientes.csv', parse_dates=['fecha_registro'])
    ordenes = pd.read_csv(raw / 'ordenes.csv', parse_dates=['fecha_orden'])
    pagos = pd.read_csv(raw / 'pagos.csv', parse_dates=['fecha_pago'])

    # Calidad y limpieza
    ordenes['monto_orden'] = ordenes['monto_orden'].fillna(ordenes['monto_orden'].median())
    pagos = pagos[pagos['estado_pago'] != 'Rechazado']

    master = (ordenes
              .merge(clientes, on='cliente_id', how='left')
              .merge(pagos, on='orden_id', how='left'))

    master['dias_pago'] = (master['fecha_pago'] - master['fecha_orden']).dt.days
    master['monto_orden'] = master['monto_orden'].round(2)

    master.to_csv(processed / 'dataset_maestro_ventas.csv', index=False)

    reporte = {
        'clientes': validar(clientes, 'clientes'),
        'ordenes': validar(ordenes, 'ordenes'),
        'pagos': validar(pagos, 'pagos_filtrado'),
        'master': validar(master, 'dataset_maestro_ventas')
    }

    with open(processed / 'data_quality_report.json', 'w', encoding='utf-8') as f:
        json.dump(reporte, f, ensure_ascii=False, indent=2)

    print('Pipeline ETL completado. Archivos en', processed)

if __name__ == '__main__':
    main()
