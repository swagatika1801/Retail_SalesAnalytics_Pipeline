import pandas as pd
import numpy as np
import os

print("=" * 60)
print("  RETAIL STORE SALES ANALYSIS")
print("=" * 60)

DATA_PATH = os.path.join(os.path.dirname(__file__), "../data/sales_data.csv")
df = pd.read_csv(DATA_PATH, parse_dates=["order_date"])

print("\n✅ Dataset loaded successfully!")

print("\n📋 First 5 Rows of Dataset:")
print(df.head().to_string(index=False))

print("\n📊 Dataset Info:")
df.info()

print("\n📈 Statistical Summary:")
print(df.describe().round(2))

df["total_sales"] = df["quantity"] * df["price"]
print("\n✅ New column 'total_sales' added (quantity × price)")

total_revenue = df["total_sales"].sum()
print(f"\n💰 Total Revenue: ₹{total_revenue:,.2f}")

most_sold = df.groupby("product")["quantity"].sum().idxmax()
most_sold_qty = df.groupby("product")["quantity"].sum().max()
print(f"\n🏆 Most Sold Product: {most_sold} ({most_sold_qty} units)")

city_sales = df.groupby("city")["total_sales"].sum().reset_index()
city_sales.columns = ["city", "total_revenue"]
city_sales = city_sales.sort_values("total_revenue", ascending=False)

print("\n🏙️  Revenue by City:")
print(city_sales.to_string(index=False))

print("\n📊 Summary Statistics for total_sales:")
print(df["total_sales"].describe().round(2))

print("\n" + "=" * 60)
print("  ADDITIONAL BUSINESS INSIGHTS")
print("=" * 60)

product_revenue = df.groupby("product")["total_sales"].sum().sort_values(ascending=False)
print("\n💡 Product-wise Revenue:")
for product, rev in product_revenue.items():
    print(f"   {product:<15} ₹{rev:>12,.2f}")

category_revenue = df.groupby("category")["total_sales"].sum().sort_values(ascending=False)
print("\n💡 Category-wise Revenue:")
for cat, rev in category_revenue.items():
    pct = (rev / total_revenue) * 100
    print(f"   {cat:<15} ₹{rev:>12,.2f}  ({pct:.1f}%)")

df["month"] = df["order_date"].dt.to_period("M")
monthly = df.groupby("month")["total_sales"].sum()
print("\n💡 Monthly Revenue Trend:")
for month, rev in monthly.items():
    print(f"   {month}  ₹{rev:>12,.2f}")

top_order = df.loc[df["total_sales"].idxmax()]
print(f"\n💡 Highest Value Order:")
print(f"   Order #{int(top_order['order_id'])} | {top_order['product']} | "
      f"{top_order['city']} | ₹{top_order['total_sales']:,.2f}")

print("\n✅ Analysis Complete!")
