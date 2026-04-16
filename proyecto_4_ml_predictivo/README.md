# Proyecto 4 — Análisis Predictivo de Churn (Machine Learning)

## Objetivo de negocio
Predecir la probabilidad de churn para priorizar acciones de retención y reducir pérdida de clientes.

## Herramientas
- Python: Pandas, Scikit-learn, Matplotlib
- SQL (integrable para scoring por segmentos)

## Estructura
- `data/`: dataset de churn y predicciones
- `models/`: modelo entrenado y métricas
- `notebooks/`: notebook explicativo
- `visualizations/`: ROC curve e importancia de variables

## Cómo ejecutar
```bash
cd /home/ubuntu/portfolio_projects/proyecto_4_ml_predictivo
python3 scripts_generate_data.py
python3 scripts_train_model.py
python3 scripts_predict.py --input data/customer_churn.csv --output data/predicciones_churn.csv
```

## Resultados clave
- Entrenamiento de 2 modelos y selección automática del mejor por ROC-AUC.
- Exportación del modelo para inferencia (`models/churn_model.pkl`).
- Predicciones batch para acciones de retención.

## Visualizaciones
- `visualizations/roc_curve.png`
- `visualizations/feature_importance.png`

## Insights y conclusiones
- Variables de uso/engagement son determinantes en churn.
- El modelo permite ranking por riesgo para campañas dirigidas.

## Próximos pasos
- Calibración de probabilidad.
- Monitoreo de drift de datos/modelo.
- Integración a pipeline ETL del proyecto 3.

## Contacto
- GitHub: https://github.com/diegoguor
- LinkedIn: https://linkedin.com/in/diego-gutiérrez-78a00b397
