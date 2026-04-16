-- Query de extracción para modelo estrella de BI
WITH ventas_base AS (
    SELECT
        v.venta_id,
        v.fecha,
        v.departamento_id,
        v.linea_negocio,
        v.ingresos,
        v.costo,
        (v.ingresos - v.costo) AS utilidad,
        CASE WHEN v.meta_ingresos = 0 THEN NULL
             ELSE (v.ingresos / v.meta_ingresos) END AS cumplimiento_meta
    FROM fact_ventas_finanzas v
)
SELECT
    vb.venta_id,
    f.anio,
    f.mes,
    f.trimestre,
    d.departamento,
    d.gerencia,
    vb.linea_negocio,
    vb.ingresos,
    vb.costo,
    vb.utilidad,
    vb.cumplimiento_meta
FROM ventas_base vb
JOIN dim_fecha f ON vb.fecha = f.fecha
JOIN dim_departamento d ON vb.departamento_id = d.departamento_id;
