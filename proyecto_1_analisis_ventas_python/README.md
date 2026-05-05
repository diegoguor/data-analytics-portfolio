# Proyecto 1 — Análisis de Ventas con Python + SQL

## Objetivo de negocio
Analizar desempeño de ventas e-commerce para identificar patrones de ingresos, rentabilidad y devoluciones por región/categoría.

## Herramientas
- Python: Pandas, Matplotlib, Seaborn
- SQL (SQLite)
- Jupyter Notebook

## Estructura
- `data/`: dataset de ventas, KPIs y resultados SQL
- `scripts/`: generación de datos, EDA y consultas SQL
- `notebooks/`: análisis narrativo
- `visualizations/`: gráficos en PNG

## Cómo ejecutar
```bash
cd /home/ubuntu/portfolio_projects/proyecto_1_analisis_ventas_python
python3 scripts/generar_datos_ventas.py
python3 scripts/eda_ventas.py
python3 scripts/consultas_sql.py
```

## Resultados clave
- Cálculo de KPIs principales (ventas, margen, devoluciones, ticket promedio).
- Segmentación por categoría, región y canal.
- Dashboard-ready charts para incluir en reportes ejecutivos.

## Visualizaciones
- `visualizations/ventas_mensuales.png`
- `visualizations/ventas_categoria.png`
- `visualizations/devoluciones_region.png`
- `visualizations/heatmap_correlacion.png`

## Insights y conclusiones
- Identificación de categorías con mayor contribución al ingreso neto.
- Regiones con mayor tasa de devolución para priorizar acciones operativas.
- Recomendación de monitoreo mensual del margen por canal.

## Próximos pasos
- Conectar a una base productiva (PostgreSQL).
- Agregar cohortes de retención por cliente.
- Incorporar forecast de ventas mensuales.

## Contacto
- GitHub: https://github.com/diegoguor
- LinkedIn: https://linkedin.com/in/diego-gutierrez-data
- Email: diego.gutierrez.o@outlook.com
