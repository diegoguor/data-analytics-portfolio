# Diseño de Proyectos de Portafolio — Analista de Datos / BI

## Proyecto 1 — Análisis de Ventas con Python + SQL

### Objetivo de negocio
Identificar patrones de ventas, comportamiento de clientes y oportunidades de crecimiento para mejorar ingresos y margen.

### Alcance técnico
- EDA completo sobre ventas e-commerce.
- Limpieza y validación de datos.
- Cálculo de KPIs (ingresos, ticket promedio, tasa de devolución, margen).
- Integración con consultas SQL para responder preguntas de negocio.

### Entregables
- `notebooks/analisis_ventas.ipynb`
- `scripts/eda_ventas.py`
- `scripts/generar_datos_ventas.py`
- `scripts/consultas_sql.py`
- Visualizaciones PNG en `visualizations/`

## Proyecto 2 — Dashboard Interactivo en Power BI

### Objetivo de negocio
Construir un dashboard ejecutivo para seguimiento de KPIs financieros y operativos, permitiendo decisiones rápidas por área.

### Alcance técnico
- Modelado estrella para Power BI.
- Definición de métricas DAX (ventas, margen, variación YoY, cumplimiento de meta).
- Storytelling por páginas (Resumen, Tendencias, Segmentos, Alertas).

### Entregables
- Dataset preparado en `data/`
- Queries en `sql_queries/`
- Guía completa de construcción en `instrucciones_dashboard_powerbi.md`
- Plantilla de documentación de métricas en `documentacion_metricas.md`

## Proyecto 3 — Pipeline ETL End-to-End

### Objetivo de negocio
Automatizar integración de datos de múltiples fuentes para generar una tabla maestra confiable para reporting.

### Alcance técnico
- Ingesta de 3 fuentes (clientes, órdenes, pagos).
- Limpieza y estandarización.
- Reglas de calidad y validaciones.
- Carga de dataset consolidado y resumen de calidad.

### Entregables
- Scripts ETL en `scripts/`
- SQL de control y análisis en `sql/`
- Datos `raw` y `processed`
- Documentación técnica y de operación

## Proyecto 4 — Análisis Predictivo con Machine Learning

### Objetivo de negocio
Predecir probabilidad de churn para priorizar acciones de retención y reducir pérdida de clientes.

### Alcance técnico
- Ingeniería de variables y preparación de datos.
- Entrenamiento de modelos de clasificación.
- Evaluación (ROC-AUC, precision, recall, F1).
- Interpretación y visualización de factores clave.

### Entregables
- `notebooks/modelo_churn.ipynb`
- `scripts/train_model.py`
- `scripts/predict.py`
- `models/churn_model.pkl`
- Visualizaciones y reporte de métricas

## Progresión de complejidad
1. **Proyecto 1:** análisis descriptivo + SQL.
2. **Proyecto 2:** BI y modelado semántico para negocio.
3. **Proyecto 3:** automatización de datos y calidad.
4. **Proyecto 4:** analítica avanzada y predicción.
