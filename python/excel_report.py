import pandas as pd
import numpy as np
import os

DATA_PATH = os.path.join(os.path.dirname(__file__), "../data/sales_data.csv")
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "../excel_output/sales_analysis.xlsx")
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

df = pd.read_csv(DATA_PATH, parse_dates=["order_date"])

# ─────────────────────────────────────────────
# Add Total Sales Column
# ─────────────────────────────────────────────
df["total_sales"] = df["quantity"] * df["price"]

# ─────────────────────────────────────────────
# Sorted by Highest Sales
# ─────────────────────────────────────────────
df_sorted = df.sort_values("total_sales", ascending=False).reset_index(drop=True)

# ─────────────────────────────────────────────
# Pivot Table: Product × City → Total Sales
# ─────────────────────────────────────────────
pivot = df.pivot_table(index="product", columns="city",
                       values="total_sales", aggfunc="sum", fill_value=0)
pivot["Grand Total"] = pivot.sum(axis=1)
pivot.loc["Grand Total"] = pivot.sum()

# ─────────────────────────────────────────────
# City Filter Views
# ─────────────────────────────────────────────
cities = df["city"].unique()
city_dfs = {city: df[df["city"] == city].reset_index(drop=True) for city in cities}

# ─────────────────────────────────────────────
# Summary Stats
# ─────────────────────────────────────────────
summary = pd.DataFrame({
    "Metric": [
        "Total Revenue",
        "Total Orders",
        "Avg Order Value",
        "Best Product",
        "Best City",
        "Best Category",
        "Highest Order Value"
    ],
    "Value": [
        f"₹{df['total_sales'].sum():,.2f}",
        str(len(df)),
        f"₹{df['total_sales'].mean():,.2f}",
        df.groupby("product")["total_sales"].sum().idxmax(),
        df.groupby("city")["total_sales"].sum().idxmax(),
        df.groupby("category")["total_sales"].sum().idxmax(),
        f"₹{df['total_sales'].max():,.2f}"
    ]
})

# ─────────────────────────────────────────────
# Write to Excel
# ─────────────────────────────────────────────
with pd.ExcelWriter(OUTPUT_PATH, engine="openpyxl") as writer:
    # Sheet 1 - Raw Data with total_sales
    df_sorted.to_excel(writer, sheet_name="Sales Data (Sorted)", index=False)

    # Sheet 2 - Pivot Table
    pivot.to_excel(writer, sheet_name="Pivot Table")

    # Sheet 3 - City Filters
    for city, city_df in city_dfs.items():
        sheet_name = f"City - {city}"[:31]
        city_df.to_excel(writer, sheet_name=sheet_name, index=False)

    # Sheet 4 - Summary
    summary.to_excel(writer, sheet_name="Summary", index=False)

    # Sheet 5 - Product Revenue Ranking
    prod_rev = df.groupby("product")["total_sales"].sum().sort_values(ascending=False).reset_index()
    prod_rev.columns = ["product", "total_revenue"]
    prod_rev.to_excel(writer, sheet_name="Product Ranking", index=False)

    # Sheet 6 - Category Revenue
    cat_rev = df.groupby("category")["total_sales"].sum().reset_index()
    cat_rev.columns = ["category", "total_revenue"]
    cat_rev["revenue_pct"] = (cat_rev["total_revenue"] / cat_rev["total_revenue"].sum() * 100).round(2)
    cat_rev.to_excel(writer, sheet_name="Category Revenue", index=False)

print(f"✅ Excel report saved: {OUTPUT_PATH}")
print("   Sheets: Sales Data, Pivot Table, City filters, Summary, Product Ranking, Category Revenue")
