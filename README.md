# 🛒 Retail Store Sales Analysis
### Capstone Project — Data Engineering | April 2026

---

## 📌 Problem Statement

A retail company sells electronic products (Laptops, Mobiles, Headphones, Keyboards) through stores in Pune, Mumbai, and Nagpur. Management noticed revenue fluctuations but lacked clarity on which products and cities drive performance. This project delivers a complete data analysis pipeline to answer those questions.

**Business Questions Answered:**
- Which products generate the most revenue?
- Which cities have the highest sales?
- Which product categories perform best?
- What are the sales trends over time?

---

## 📁 Project Structure

```
retail_sales_analysis/
├── data/
│   └── sales_data.csv          # Transaction dataset (30 orders)
├── sql/
│   └── queries.sql             # All 7 SQL queries + bonus queries
├── python/
│   ├── analysis.py             # Pandas-based analysis pipeline
│   ├── visualizations.py       # Bar, Pie, Line, Grouped Bar charts
│   ├── sql_runner.py           # SQL execution via SQLite
│   ├── excel_report.py         # Excel workbook generator
│   └── generate_pdf.py         # PDF documentation generator
├── visualizations/             # Generated chart images (PNG)
├── excel_output/
│   └── sales_analysis.xlsx     # Multi-sheet Excel report
├── docs/
│   └── project_documentation.pdf  # 7-page project PDF
├── main.py                     # 🚀 Run everything in one command
├── requirements.txt
└── README.md
```

---

## 🚀 Quick Start

```bash
# 1. Clone the repo
git clone https://github.com/Kanhaiyathakur001/retail-sales-analysis.git
cd retail-sales-analysis

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the complete pipeline
python main.py
```

---

## 📊 Dataset

**File:** `data/sales_data.csv`

| Column | Type | Description |
|--------|------|-------------|
| order_id | int | Unique order identifier |
| order_date | date | Purchase date |
| city | string | Pune / Mumbai / Nagpur |
| product | string | Laptop / Mobile / Headphones / Keyboard |
| category | string | Electronics / Accessories |
| quantity | int | Units sold |
| price | decimal | Unit price (₹) |

---

## 🗄️ SQL Analysis (`sql/queries.sql`)

| # | Query | Result |
|---|-------|--------|
| 1 | Display all sales records | 30 rows |
| 2 | Total sales revenue | ₹12,92,500 |
| 3 | Top-selling product by quantity | Keyboard (35 units) |
| 4 | Revenue by city | Pune ₹5.38L › Mumbai ₹4.53L › Nagpur ₹3L |
| 5 | Category-wise revenue | Electronics 91.3% │ Accessories 8.7% |
| 6 | Highest-value order | Order #1013 — Laptop, Pune — ₹1,50,000 |
| 7 | Average product price | Laptop ₹50K │ Mobile ₹20K │ Headphones ₹2K │ Keyboard ₹1.5K |

---

## 🐍 Python Analysis (`python/analysis.py`)

Steps implemented:
1. Load dataset with `pd.read_csv()`
2. Display first rows with `.head()`
3. Inspect structure with `.info()` and `.describe()`
4. Create `total_sales` column (`quantity × price`)
5. Calculate total revenue
6. Identify most sold product
7. Group sales by city
8. Calculate summary statistics

---

## 📈 Visualizations

| Chart | File |
|-------|------|
| Bar Chart — Product vs Total Sales | `bar_chart_product_sales.png` |
| Pie Chart — Category Distribution | `pie_chart_category_sales.png` |
| Line Chart — Sales Trend by Date | `line_chart_sales_by_date.png` |
| Grouped Bar — City vs Product Revenue | `grouped_bar_city_product.png` |

---

## 📊 Excel Report (`excel_output/sales_analysis.xlsx`)

Sheets included:
- **Sales Data (Sorted)** — Dataset with `total_sales` column, sorted by value
- **Pivot Table** — Product × City revenue breakdown
- **City - Pune / Mumbai / Nagpur** — City-filtered views
- **Summary** — 7 key business KPIs
- **Product Ranking** — Products ranked by total revenue
- **Category Revenue** — Category breakdown with percentages

---

## 🔑 Key Findings

| Insight | Detail |
|---------|--------|
| 💰 Total Revenue | ₹12,92,500 |
| 🏆 Top Product (Revenue) | Laptop — ₹7,00,000 (54.2%) |
| 📦 Top Product (Volume) | Keyboard — 35 units |
| 🏙️ Top City | Pune — ₹5,38,500 (41.7%) |
| 📂 Top Category | Electronics — 91.3% of revenue |
| 📅 Best Month | January 2025 — ₹7,71,000 |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.10+ | Core language |
| Pandas | Data manipulation |
| NumPy | Numerical operations |
| Matplotlib | Visualizations |
| SQLite (stdlib) | SQL query execution |
| OpenPyXL | Excel report generation |
| ReportLab | PDF documentation |
| Git / GitHub | Version control |

---

## 📄 Project Documentation

A complete 7-page PDF report is available at `docs/project_documentation.pdf` including:
- Cover page with KPIs
- Problem statement & dataset schema
- All SQL queries with results
- Python analysis steps & findings
- All 4 visualizations
- Excel pivot table output
- Tech stack & future improvements
- Business insights & recommendations

---

## 👨‍💻 Author
\
**Swagatika Barik**  

---

*This project is original work submitted for the Capstone Project evaluation.*
