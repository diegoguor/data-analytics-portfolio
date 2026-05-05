# Proyecto 3 — Pipeline ETL End-to-End

## Objetivo de negocio
Automatizar la consolidación de múltiples fuentes de datos para disponer de una tabla maestra confiable para reporting y análisis.

## Herramientas
- Python (Pandas)
- SQL
- Archivos CSV como staging

## Estructura
- `data/raw/`: fuentes simuladas (clientes, órdenes, pagos)
- `data/processed/`: dataset maestro y reporte de calidad
- `scripts/`: generación e integración ETL
- `sql/`: consultas de análisis
- `visualizations/`: gráficos de validación

## Cómo ejecutar
```bash
cd /home/ubuntu/portfolio_projects/proyecto_3_pipeline_etl
python3 scripts/generar_fuentes_raw.py
python3 scripts/etl_pipeline.py
```

## Resultados clave
- Consolidación de 3 fuentes en un dataset maestro único.
- Reporte de calidad de datos con nulos, duplicados y volumen.
- Base preparada para dashboarding o modelos analíticos.

## Visualizaciones
- `visualizations/ingreso_por_segmento.png`

## Insights y conclusiones
- Segmentos con mayor aporte al ingreso.
- Calidad de datos controlada por reglas explícitas.
- Pipeline reutilizable para ejecuciones periódicas.

## Próximos pasos
- Migrar a orquestación con Airflow/ADF.
- Agregar pruebas unitarias de calidad (Great Expectations).
- Cargar resultados a DW en cloud.

## Contacto
- GitHub: https://github.com/diegoguor
- LinkedIn: https://linkedin.com/in/diego-gutierrez-data
- Email: diego.gutierrez.o@outlook.com
