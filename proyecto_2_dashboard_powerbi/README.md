# Proyecto 2 — Dashboard Interactivo en Power BI

## Objetivo de negocio
Construir un dashboard ejecutivo de desempeño financiero para seguimiento de KPIs, comparación temporal y cumplimiento de metas.

## Herramientas
- Power BI (DAX, Power Query)
- SQL (consultas de extracción)
- CSV modelado en esquema estrella

## Estructura
- `data/`: fact table + dimensiones
- `sql_queries/`: consulta para extracción/modelado
- `powerbi/`: mockups visuales y notas para .pbix
- `documentacion_metricas.md`: catálogo DAX

## Cómo replicar
1. Cargar tablas de `data/` en Power BI.
2. Crear relaciones según `documentacion_metricas.md`.
3. Crear medidas DAX base y temporales.
4. Construir páginas de dashboard (Resumen, Tendencias, Segmentación, Alertas).

## Resultados clave
- Modelo listo para crear un dashboard ejecutivo en menos de 1 hora.
- Métricas DAX priorizadas para entrevistas y casos prácticos BI.
- Estructura adaptable a múltiples industrias.

## Visualizaciones (mockups)
- `powerbi/mockup_tendencia_ingresos.png`
- `powerbi/mockup_utilidad_departamento.png`

## Insights esperados
- Variaciones intermensuales y YoY.
- Departamentos con mayor contribución de utilidad.
- Brechas de cumplimiento frente a meta.

## Próximos pasos
- Publicar en Power BI Service.
- Implementar RLS (Row-Level Security).
- Integrar refresh incremental.

## Contacto
- GitHub: https://github.com/diegoguor
- LinkedIn: https://linkedin.com/in/diego-gutierrez-data
- Email: diego.gutierrez.o@outlook.com
