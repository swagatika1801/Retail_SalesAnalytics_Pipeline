"""
============================================================
Retail Store Sales Analysis - Visualizations
Author: Kanhaiya Thakur
Description: Bar, Pie, and Line charts using Matplotlib
============================================================
"""

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import os

# ─────────────────────────────────────────────
# Load Data
# ─────────────────────────────────────────────
DATA_PATH = os.path.join(os.path.dirname(__file__), "../data/sales_data.csv")
df = pd.read_csv(DATA_PATH, parse_dates=["order_date"])
df["total_sales"] = df["quantity"] * df["price"]
df["month"] = df["order_date"].dt.to_period("M").astype(str)

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "../visualizations")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ─────────────────────────────────────────────
# Colour palette
# ─────────────────────────────────────────────
COLORS = ["#4C72B0", "#DD8452", "#55A868", "#C44E52", "#8172B3"]
ACCENT = "#4C72B0"

# ─────────────────────────────────────────────
# CHART 1: Bar Chart – Product vs Total Sales
# ─────────────────────────────────────────────
product_sales = df.groupby("product")["total_sales"].sum().sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(product_sales.index, product_sales.values, color=COLORS, edgecolor="white", linewidth=0.8)
ax.set_title("Product vs Total Sales Revenue", fontsize=16, fontweight="bold", pad=15)
ax.set_xlabel("Product", fontsize=13)
ax.set_ylabel("Total Sales (₹)", fontsize=13)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"₹{x/1e5:.1f}L"))
ax.set_facecolor("#f8f9fa")
fig.patch.set_facecolor("#ffffff")
ax.grid(axis="y", linestyle="--", alpha=0.5)
ax.spines[["top", "right"]].set_visible(False)

for bar in bars:
    height = bar.get_height()
    ax.annotate(f"₹{height/1000:.0f}K",
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 6), textcoords="offset points",
                ha="center", va="bottom", fontsize=10, fontweight="bold")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "bar_chart_product_sales.png"), dpi=150, bbox_inches="tight")
plt.close()
print("✅ Bar chart saved: bar_chart_product_sales.png")

# ─────────────────────────────────────────────
# CHART 2: Pie Chart – Category Sales Distribution
# ─────────────────────────────────────────────
category_sales = df.groupby("category")["total_sales"].sum()

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    category_sales.values,
    labels=category_sales.index,
    autopct="%1.1f%%",
    colors=["#4C72B0", "#DD8452"],
    startangle=140,
    explode=[0.05] * len(category_sales),
    shadow=True,
    wedgeprops={"edgecolor": "white", "linewidth": 2}
)
for text in texts:
    text.set_fontsize(13)
    text.set_fontweight("bold")
for autotext in autotexts:
    autotext.set_fontsize(12)
    autotext.set_fontweight("bold")
    autotext.set_color("white")

ax.set_title("Category-wise Sales Distribution", fontsize=16, fontweight="bold", pad=20)
total = category_sales.sum()
legend_labels = [f"{cat}: ₹{val/1000:.0f}K" for cat, val in category_sales.items()]
ax.legend(wedges, legend_labels, loc="lower center", bbox_to_anchor=(0.5, -0.1),
          fontsize=11, frameon=True)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "pie_chart_category_sales.png"), dpi=150, bbox_inches="tight")
plt.close()
print("✅ Pie chart saved: pie_chart_category_sales.png")

# ─────────────────────────────────────────────
# CHART 3: Line Chart – Sales by Date
# ─────────────────────────────────────────────
daily_sales = df.groupby("order_date")["total_sales"].sum().reset_index()
daily_sales = daily_sales.sort_values("order_date")

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(daily_sales["order_date"], daily_sales["total_sales"],
        marker="o", color=ACCENT, linewidth=2.5, markersize=7,
        markerfacecolor="white", markeredgewidth=2, markeredgecolor=ACCENT)
ax.fill_between(daily_sales["order_date"], daily_sales["total_sales"],
                alpha=0.12, color=ACCENT)

ax.set_title("Daily Sales Trend", fontsize=16, fontweight="bold", pad=15)
ax.set_xlabel("Date", fontsize=13)
ax.set_ylabel("Total Sales (₹)", fontsize=13)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"₹{x/1000:.0f}K"))
ax.set_facecolor("#f8f9fa")
fig.patch.set_facecolor("#ffffff")
ax.grid(linestyle="--", alpha=0.5)
ax.spines[["top", "right"]].set_visible(False)
plt.xticks(rotation=45, ha="right")

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "line_chart_sales_by_date.png"), dpi=150, bbox_inches="tight")
plt.close()
print("✅ Line chart saved: line_chart_sales_by_date.png")

# ─────────────────────────────────────────────
# CHART 4 (Bonus): Grouped Bar – City vs Product Revenue
# ─────────────────────────────────────────────
pivot = df.pivot_table(index="product", columns="city", values="total_sales", aggfunc="sum").fillna(0)

x = np.arange(len(pivot.index))
width = 0.25
fig, ax = plt.subplots(figsize=(12, 6))

for i, (city, color) in enumerate(zip(pivot.columns, COLORS)):
    offset = (i - 1) * width
    bars = ax.bar(x + offset, pivot[city], width, label=city, color=color, edgecolor="white")

ax.set_title("Product Revenue by City", fontsize=16, fontweight="bold", pad=15)
ax.set_xlabel("Product", fontsize=13)
ax.set_ylabel("Revenue (₹)", fontsize=13)
ax.set_xticks(x)
ax.set_xticklabels(pivot.index, fontsize=12)
ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"₹{x/1000:.0f}K"))
ax.legend(title="City", fontsize=11)
ax.set_facecolor("#f8f9fa")
fig.patch.set_facecolor("#ffffff")
ax.grid(axis="y", linestyle="--", alpha=0.5)
ax.spines[["top", "right"]].set_visible(False)

plt.tight_layout()
plt.savefig(os.path.join(OUTPUT_DIR, "grouped_bar_city_product.png"), dpi=150, bbox_inches="tight")
plt.close()
print("✅ Grouped bar chart saved: grouped_bar_city_product.png")

print("\n🎉 All visualizations generated in /visualizations/")
