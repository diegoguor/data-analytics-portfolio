"""Ejecuta consultas SQL de negocio sobre SQLite."""
import sqlite3
from pathlib import Path
import pandas as pd

QUERIES = {
    "top_5_clientes": """
        SELECT customer_id, ROUND(SUM(net_sales),2) AS ventas_netas
        FROM sales
        GROUP BY customer_id
        ORDER BY ventas_netas DESC
        LIMIT 5;
    """,
    "ventas_por_canal": """
        SELECT channel,
               COUNT(DISTINCT order_id) AS ordenes,
               ROUND(SUM(net_sales),2) AS ventas,
               ROUND(AVG(net_sales),2) AS ticket_promedio
        FROM sales
        GROUP BY channel
        ORDER BY ventas DESC;
    """,
    "margen_por_categoria": """
        SELECT category,
               ROUND(SUM(net_sales),2) AS ventas,
               ROUND(SUM(profit),2) AS utilidad,
               ROUND((SUM(profit)/SUM(net_sales))*100,2) AS margen_pct
        FROM sales
        GROUP BY category
        ORDER BY margen_pct DESC;
    """
}


def main():
    root = Path(__file__).resolve().parents[1]
    conn = sqlite3.connect(root / "data" / "sales_ecommerce.db")

    output_file = root / "data" / "resultados_sql.md"
    lines = ["# Resultados de consultas SQL\n"]

    for name, query in QUERIES.items():
        df = pd.read_sql_query(query, conn)
        lines.append(f"## {name}\n")
        lines.append(df.to_markdown(index=False))
        lines.append("\n")

    conn.close()
    output_file.write_text("\n".join(lines), encoding="utf-8")
    print(f"Resultados guardados en {output_file}")


if __name__ == "__main__":
    main()
