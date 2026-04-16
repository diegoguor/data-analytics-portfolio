# Documentación de Métricas — Dashboard Power BI

## Tabla de medidas DAX sugeridas

```DAX
Ventas Totales = SUM(fact_ventas_finanzas[ingresos])

Costo Total = SUM(fact_ventas_finanzas[costo])

Utilidad Total = [Ventas Totales] - [Costo Total]

Margen % = DIVIDE([Utilidad Total], [Ventas Totales], 0)

Meta Ventas = SUM(fact_ventas_finanzas[meta_ingresos])

Cumplimiento Meta % = DIVIDE([Ventas Totales], [Meta Ventas], 0)

Ventas YoY =
CALCULATE(
    [Ventas Totales],
    DATEADD(dim_fecha[fecha], -1, YEAR)
)

Variación YoY % = DIVIDE([Ventas Totales] - [Ventas YoY], [Ventas YoY], 0)

Ticket Promedio = DIVIDE([Ventas Totales], DISTINCTCOUNT(fact_ventas_finanzas[venta_id]), 0)
```

## Reglas de modelado
- Relación uno-a-muchos: `dim_fecha -> fact_ventas_finanzas`.
- Relación uno-a-muchos: `dim_departamento -> fact_ventas_finanzas`.
- Modelo estrella, evitar relaciones bidireccionales innecesarias.

## Páginas recomendadas
1. **Resumen Ejecutivo**: KPIs (ventas, utilidad, margen, cumplimiento).
2. **Tendencias**: evolución mensual y comparación YoY.
3. **Segmentación**: línea de negocio, departamento, gerencia.
4. **Alertas**: focos bajo meta y caídas intermensuales.
