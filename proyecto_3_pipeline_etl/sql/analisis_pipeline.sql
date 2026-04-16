-- Ejemplos de queries analíticas para dataset maestro

-- 1) Ingreso total por segmento
SELECT segmento, ROUND(SUM(monto_orden),2) AS ingreso_total
FROM dataset_maestro_ventas
GROUP BY segmento
ORDER BY ingreso_total DESC;

-- 2) Ticket promedio por canal
SELECT canal, ROUND(AVG(monto_orden),2) AS ticket_promedio
FROM dataset_maestro_ventas
GROUP BY canal
ORDER BY ticket_promedio DESC;

-- 3) Tiempo promedio de pago por método
SELECT metodo_pago, ROUND(AVG(dias_pago),2) AS dias_promedio_pago
FROM dataset_maestro_ventas
GROUP BY metodo_pago
ORDER BY dias_promedio_pago;
