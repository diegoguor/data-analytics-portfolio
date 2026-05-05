# Instrucciones Generales del Portafolio y Guías Paso a Paso

## 1) Proyecto 1 — Python + SQL (EDA)
1. Crear entorno virtual e instalar dependencias: `pip install -r requirements.txt`.
2. Ejecutar `scripts/generar_datos_ventas.py` para construir dataset y SQLite.
3. Ejecutar `scripts/eda_ventas.py` para generar KPIs y visualizaciones.
4. Ejecutar `scripts/consultas_sql.py` para resultados SQL en markdown.
5. Abrir `notebooks/analisis_ventas.ipynb` para narrativa y presentación.

## 2) Proyecto 2 — Dashboard Power BI (sin .pbix preconstruido)

### Caso A: Construcción desde CSV
1. Abrir Power BI Desktop > **Obtener datos > Texto/CSV**.
2. Cargar:
   - `data/fact_ventas_finanzas.csv`
   - `data/dim_fecha.csv`
   - `data/dim_departamento.csv`
3. En **Modelado**, crear relaciones:
   - `dim_fecha[fecha]` 1:* `fact_ventas_finanzas[fecha]`
   - `dim_departamento[departamento_id]` 1:* `fact_ventas_finanzas[departamento_id]`
4. Marcar `dim_fecha` como tabla de fechas.

### Caso B: Construcción desde SQL
1. Cargar tablas en tu motor SQL favorito (PostgreSQL o SQL Server).
2. Ejecutar query de `sql_queries/extraccion_modelo_estrella.sql`.
3. Conectar Power BI a la vista/tabla resultante.

### Medidas DAX paso a paso
1. Crear carpeta de medidas `Medidas_KPI`.
2. Crear medidas base:
   - `Ventas Totales = SUM(fact_ventas_finanzas[ingresos])`
   - `Costo Total = SUM(fact_ventas_finanzas[costo])`
   - `Utilidad Total = [Ventas Totales]-[Costo Total]`
3. Crear indicadores:
   - `Margen % = DIVIDE([Utilidad Total],[Ventas Totales],0)`
   - `Meta Ventas = SUM(fact_ventas_finanzas[meta_ingresos])`
   - `Cumplimiento Meta % = DIVIDE([Ventas Totales],[Meta Ventas],0)`
4. Crear inteligencia temporal:
   - `Ventas YoY = CALCULATE([Ventas Totales], DATEADD(dim_fecha[fecha], -1, YEAR))`
   - `Variación YoY % = DIVIDE([Ventas Totales]-[Ventas YoY],[Ventas YoY],0)`
5. Aplicar formato a porcentajes y moneda.

### Guía de desarrollo del dashboard
- **Página 1 (Resumen Ejecutivo):** tarjetas de KPIs + tendencia mensual.
- **Página 2 (Segmentación):** barras por departamento y línea de negocio.
- **Página 3 (Cumplimiento):** semáforos/meta por departamento + tabla de detalle.
- **Página 4 (Alertas):** filtros por mes/año y análisis de caída vs YoY.

## 3) Proyecto 3 — Pipeline ETL
1. Ejecutar `scripts/generar_fuentes_raw.py`.
2. Validar archivos en `data/raw/`.
3. Ejecutar `scripts/etl_pipeline.py`.
4. Revisar `data/processed/dataset_maestro_ventas.csv` y `data_quality_report.json`.
5. Usar `sql/analisis_pipeline.sql` para consultas de negocio.

## 4) Proyecto 4 — Machine Learning Predictivo
1. Instalar dependencias de `requirements.txt`.
2. Ejecutar `scripts_generate_data.py`.
3. Ejecutar `scripts_train_model.py`.
4. Revisar outputs en `models/` y `visualizations/`.
5. Para scoring batch:
   `python scripts_predict.py --input data/customer_churn.csv --output data/predicciones_churn.csv`

## 5) Buenas prácticas de presentación
- Mostrar objetivo de negocio antes de detalles técnicos.
- Resaltar impacto medible (tiempo, costo, precisión, adopción).
- Explicar decisiones técnicas con trade-offs.

## Contacto
- GitHub: https://github.com/diegoguor
- LinkedIn: https://linkedin.com/in/diego-gutierrez-data
- Email: diego.gutierrez.o@outlook.com
