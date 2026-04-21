"""
============================================================
Retail Store Sales Analysis - SQL Analysis via SQLite
Author: Kanhaiya Thakur
Description: Execute all SQL queries programmatically
============================================================
"""

import sqlite3
import pandas as pd
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "../data/sales_data.csv")

# ─────────────────────────────────────────────
# Setup SQLite In-Memory Database
# ─────────────────────────────────────────────
conn = sqlite3.connect(":memory:")
df = pd.read_csv(DATA_PATH, parse_dates=["order_date"])
df["order_date"] = df["order_date"].dt.strftime("%Y-%m-%d")
df.to_sql("sales", conn, index=False, if_exists="replace")
print("✅ SQLite database created and data loaded.\n")

def run_query(title, sql):
    print(f"{'─'*60}")
    print(f"  {title}")
    print(f"{'─'*60}")
    result = pd.read_sql_query(sql, conn)
    print(result.to_string(index=False))
    print()
    return result

# ─────────────────────────────────────────────
# QUERY 1: All Sales Records
# ─────────────────────────────────────────────
run_query("QUERY 1: All Sales Records", "SELECT * FROM sales LIMIT 10")

# ─────────────────────────────────────────────
# QUERY 2: Total Revenue
# ─────────────────────────────────────────────
run_query("QUERY 2: Total Sales Revenue",
    "SELECT ROUND(SUM(quantity * price), 2) AS total_revenue FROM sales")

# ─────────────────────────────────────────────
# QUERY 3: Top-Selling Product by Quantity
# ─────────────────────────────────────────────
run_query("QUERY 3: Top-Selling Product by Quantity",
    """SELECT product, SUM(quantity) AS total_quantity_sold
       FROM sales GROUP BY product
       ORDER BY total_quantity_sold DESC LIMIT 1""")

# ─────────────────────────────────────────────
# QUERY 4: Revenue by City
# ─────────────────────────────────────────────
run_query("QUERY 4: Revenue by City",
    """SELECT city, ROUND(SUM(quantity * price), 2) AS city_revenue
       FROM sales GROUP BY city ORDER BY city_revenue DESC""")

# ─────────────────────────────────────────────
# QUERY 5: Category-wise Revenue
# ─────────────────────────────────────────────
run_query("QUERY 5: Category-wise Revenue",
    """SELECT category,
              ROUND(SUM(quantity * price), 2) AS category_revenue,
              ROUND(SUM(quantity * price) * 100.0 / (SELECT SUM(quantity * price) FROM sales), 2) AS pct
       FROM sales GROUP BY category ORDER BY category_revenue DESC""")

# ─────────────────────────────────────────────
# QUERY 6: Highest-Value Order
# ─────────────────────────────────────────────
run_query("QUERY 6: Highest-Value Order",
    """SELECT order_id, order_date, city, product, quantity, price,
              (quantity * price) AS order_value
       FROM sales ORDER BY order_value DESC LIMIT 1""")

# ─────────────────────────────────────────────
# QUERY 7: Average Product Price
# ─────────────────────────────────────────────
run_query("QUERY 7: Average Product Price",
    """SELECT product, ROUND(AVG(price), 2) AS avg_price
       FROM sales GROUP BY product ORDER BY avg_price DESC""")

conn.close()
print("✅ All SQL queries executed successfully!")
