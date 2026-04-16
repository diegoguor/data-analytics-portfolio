# Instrucciones Paso a Paso — Dashboard Power BI + DAX

## 1. Preparación
1. Abre Power BI Desktop.
2. Ve a **Obtener datos > Texto/CSV**.
3. Importa estos archivos:
   - `data/fact_ventas_finanzas.csv`
   - `data/dim_fecha.csv`
   - `data/dim_departamento.csv`

## 2. Modelado de datos (esquema estrella)
1. En vista **Modelo**, crea relaciones:
   - `dim_fecha[fecha]` (1) -> `fact_ventas_finanzas[fecha]` (*)
   - `dim_departamento[departamento_id]` (1) -> `fact_ventas_finanzas[departamento_id]` (*)
2. Marca `dim_fecha` como **Tabla de fechas**.
3. Verifica direccionalidad simple (single direction) para mejor performance.

## 3. Medidas DAX (orden recomendado)
```DAX
Ventas Totales = SUM(fact_ventas_finanzas[ingresos])
Costo Total = SUM(fact_ventas_finanzas[costo])
Utilidad Total = [Ventas Totales] - [Costo Total]
Margen % = DIVIDE([Utilidad Total], [Ventas Totales], 0)
Meta Ventas = SUM(fact_ventas_finanzas[meta_ingresos])
Cumplimiento Meta % = DIVIDE([Ventas Totales], [Meta Ventas], 0)
Ventas YoY = CALCULATE([Ventas Totales], DATEADD(dim_fecha[fecha], -1, YEAR))
Variación YoY % = DIVIDE([Ventas Totales] - [Ventas YoY], [Ventas YoY], 0)
Ticket Promedio = DIVIDE([Ventas Totales], DISTINCTCOUNT(fact_ventas_finanzas[venta_id]), 0)
```

## 4. Diseño del dashboard
### Página 1: Resumen Ejecutivo
- Tarjetas: Ventas Totales, Utilidad Total, Margen %, Cumplimiento Meta %.
- Línea: tendencia mensual de ingresos.
- Segmentadores: Año, Trimestre, Departamento.

### Página 2: Segmentación
- Barras: utilidad por departamento.
- Barras apiladas: ventas por línea de negocio.
- Tabla detalle por departamento y línea.

### Página 3: Cumplimiento y alertas
- KPI semáforo de Cumplimiento Meta %.
- Tabla con departamentos por debajo de 95% de meta.
- Visual de variación YoY para detectar caídas.

## 5. Recomendaciones de performance
- Evita columnas calculadas innecesarias; usa medidas.
- Desactiva Auto Date/Time si usas `dim_fecha`.
- Usa nombres claros de medidas con prefijo `KPI_`.

## 6. Validación final
- Compara resultados con cálculo manual en Excel para 2-3 muestras.
- Verifica filtros cruzados entre visuales.
- Documenta supuestos de negocio en `documentacion_metricas.md`.
