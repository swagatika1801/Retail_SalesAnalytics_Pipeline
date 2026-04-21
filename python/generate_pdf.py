from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib.colors import HexColor, black, white
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, Image, PageBreak, HRFlowable)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib import colors
import os

BASE = os.path.dirname(os.path.abspath(__file__))
VIZ_DIR = os.path.join(BASE, "../visualizations")
OUTPUT = os.path.join(BASE, "../docs/project_documentation.pdf")
os.makedirs(os.path.dirname(OUTPUT), exist_ok=True)

# ─── Colours ───────────────────────────────────────────────
BLUE      = HexColor("#1a3c6e")
ACCENT    = HexColor("#4C72B0")
LIGHT_BG  = HexColor("#EEF2F8")
GOLD      = HexColor("#F0A500")
GRAY      = HexColor("#555555")
TABLE_HDR = HexColor("#1a3c6e")

# ─── Document ──────────────────────────────────────────────
doc = SimpleDocTemplate(
    OUTPUT, pagesize=A4,
    leftMargin=2*cm, rightMargin=2*cm,
    topMargin=2.5*cm, bottomMargin=2.5*cm
)

styles = getSampleStyleSheet()

def S(name, **kw):
    return ParagraphStyle(name, parent=styles["Normal"], **kw)

title_style   = S("T",  fontSize=24, fontName="Helvetica-Bold", textColor=BLUE,    alignment=TA_CENTER, spaceAfter=6)
sub_style     = S("ST", fontSize=13, fontName="Helvetica",      textColor=GRAY,    alignment=TA_CENTER, spaceAfter=4)
h1_style      = S("H1", fontSize=15, fontName="Helvetica-Bold", textColor=BLUE,    spaceBefore=14, spaceAfter=6)
h2_style      = S("H2", fontSize=12, fontName="Helvetica-Bold", textColor=ACCENT,  spaceBefore=10, spaceAfter=4)
body_style    = S("B",  fontSize=10, fontName="Helvetica",      textColor=black,   leading=15, alignment=TA_JUSTIFY, spaceAfter=6)
bullet_style  = S("BL", fontSize=10, fontName="Helvetica",      textColor=black,   leading=14, leftIndent=14, bulletIndent=4, spaceAfter=3)
code_style    = S("C",  fontSize=8,  fontName="Courier",         textColor=HexColor("#1a1a2e"), backColor=HexColor("#f0f4ff"),
                   leading=12, leftIndent=10, rightIndent=10, borderPad=4, spaceAfter=6)
insight_style = S("I",  fontSize=10, fontName="Helvetica-Oblique", textColor=BLUE, leading=14, leftIndent=10, spaceAfter=4)
center_style  = S("CN", fontSize=10, fontName="Helvetica",      alignment=TA_CENTER, spaceAfter=4)

story = []

# ─────────────────────────────────────────────────────────────
# PAGE 1 – COVER
# ─────────────────────────────────────────────────────────────
story.append(Spacer(1, 2*cm))

# Title block
cover_data = [[Paragraph("RETAIL STORE SALES ANALYSIS", S("CT",
    fontSize=22, fontName="Helvetica-Bold", textColor=white, alignment=TA_CENTER))],
    [Paragraph("Capstone Project Documentation", S("CST",
    fontSize=13, fontName="Helvetica", textColor=HexColor("#c8d6f0"), alignment=TA_CENTER))]]
cover_tbl = Table(cover_data, colWidths=[17*cm])
cover_tbl.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), BLUE),
    ("TOPPADDING",    (0,0), (-1,0), 20),
    ("BOTTOMPADDING", (0,0), (-1,0), 6),
    ("TOPPADDING",    (0,1), (-1,1), 4),
    ("BOTTOMPADDING", (0,1), (-1,-1), 20),
    ("ROUNDEDCORNERS", [8]),
]))
story.append(cover_tbl)
story.append(Spacer(1, 0.6*cm))

# KPI strip
kpi_data = [
    [Paragraph("₹12.93L\nTotal Revenue",   center_style),
     Paragraph("30\nOrders",               center_style),
     Paragraph("Laptop\nTop Product",      center_style),
     Paragraph("Pune\nTop City",           center_style)]
]
kpi_tbl = Table(kpi_data, colWidths=[4.25*cm]*4)
kpi_tbl.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), LIGHT_BG),
    ("FONTNAME",   (0,0), (-1,-1), "Helvetica-Bold"),
    ("FONTSIZE",   (0,0), (-1,-1), 10),
    ("ALIGN",      (0,0), (-1,-1), "CENTER"),
    ("VALIGN",     (0,0), (-1,-1), "MIDDLE"),
    ("TOPPADDING",    (0,0),(-1,-1), 10),
    ("BOTTOMPADDING", (0,0),(-1,-1), 10),
    ("GRID", (0,0),(-1,-1), 0.5, HexColor("#c0cce0")),
    ("ROUNDEDCORNERS", [6]),
]))
story.append(kpi_tbl)
story.append(Spacer(1, 0.6*cm))

# Meta info table
meta_data = [
    ["Student Name",  "Kanhaiya Thakur",   "Roll Number",  "——"],
    ["Batch/Program", "Data Engineering",  "Submission",   "April 21, 2026"],
    ["Tech Stack",    "Python · SQL · Excel · Matplotlib", "GitHub", "github.com/Kanhaiyathakur001"],
]
meta_tbl = Table(meta_data, colWidths=[3.5*cm, 5*cm, 3*cm, 5.5*cm])
meta_tbl.setStyle(TableStyle([
    ("FONTNAME",   (0,0), (-1,-1), "Helvetica"),
    ("FONTNAME",   (0,0), (0,-1), "Helvetica-Bold"),
    ("FONTNAME",   (2,0), (2,-1), "Helvetica-Bold"),
    ("FONTSIZE",   (0,0), (-1,-1), 9),
    ("BACKGROUND", (0,0), (0,-1), LIGHT_BG),
    ("BACKGROUND", (2,0), (2,-1), LIGHT_BG),
    ("GRID", (0,0),(-1,-1), 0.4, HexColor("#c0cce0")),
    ("TOPPADDING",    (0,0),(-1,-1), 6),
    ("BOTTOMPADDING", (0,0),(-1,-1), 6),
    ("LEFTPADDING",   (0,0),(-1,-1), 8),
]))
story.append(meta_tbl)
story.append(PageBreak())

# ─────────────────────────────────────────────────────────────
# PAGE 2 – PROBLEM STATEMENT & DATASET
# ─────────────────────────────────────────────────────────────
story.append(Paragraph("1. Problem Statement", h1_style))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=8))
story.append(Paragraph(
    "A retail company sells electronic products — Laptops, Mobiles, Headphones, and Keyboards — "
    "through stores in Pune, Mumbai, and Nagpur. Management noticed revenue fluctuations but lacked "
    "data-driven insight into which products and cities drive performance. This project delivers a "
    "complete analysis answering four core business questions:", body_style))

qs = ["Which products generate the most revenue?",
      "Which cities have the highest sales volume?",
      "Which product categories perform best?",
      "What are the sales trends over time?"]
for q in qs:
    story.append(Paragraph(f"• {q}", bullet_style))

story.append(Spacer(1, 0.4*cm))
story.append(Paragraph("2. Dataset Overview", h1_style))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=8))
story.append(Paragraph(
    "The dataset (sales_data.csv) contains 30 transactional records spanning January–February 2025 "
    "across 3 cities, 4 products, and 2 categories.", body_style))

schema_data = [
    ["Column", "Type", "Description"],
    ["order_id",   "INTEGER", "Unique order identifier"],
    ["order_date", "DATE",    "Date of purchase"],
    ["city",       "VARCHAR", "Store location (Pune / Mumbai / Nagpur)"],
    ["product",    "VARCHAR", "Product name"],
    ["category",   "VARCHAR", "Electronics / Accessories"],
    ["quantity",   "INTEGER", "Units sold"],
    ["price",      "DECIMAL", "Unit price in ₹"],
]
schema_tbl = Table(schema_data, colWidths=[3.5*cm, 2.5*cm, 11*cm])
schema_tbl.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,0), TABLE_HDR),
    ("TEXTCOLOR",     (0,0), (-1,0), white),
    ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",      (0,0), (-1,-1), 9),
    ("BACKGROUND",    (0,1), (-1,-1), white),
    ("ROWBACKGROUNDS",(0,1), (-1,-1), [white, LIGHT_BG]),
    ("GRID",          (0,0), (-1,-1), 0.4, HexColor("#c0cce0")),
    ("TOPPADDING",    (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ("LEFTPADDING",   (0,0), (-1,-1), 8),
]))
story.append(schema_tbl)
story.append(PageBreak())

# ─────────────────────────────────────────────────────────────
# PAGE 3 – SQL ANALYSIS
# ─────────────────────────────────────────────────────────────
story.append(Paragraph("3. SQL Analysis", h1_style))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=8))

sql_tasks = [
    ("Display All Sales Records",             "SELECT * FROM sales;"),
    ("Total Sales Revenue",                   "SELECT ROUND(SUM(quantity * price), 2) AS total_revenue FROM sales;"),
    ("Top-Selling Product by Quantity",       "SELECT product, SUM(quantity) AS total_qty\nFROM sales GROUP BY product\nORDER BY total_qty DESC LIMIT 1;"),
    ("Revenue by City",                       "SELECT city, ROUND(SUM(quantity * price), 2) AS city_revenue\nFROM sales GROUP BY city ORDER BY city_revenue DESC;"),
    ("Category-wise Revenue",                 "SELECT category, ROUND(SUM(quantity*price),2) AS revenue,\nROUND(SUM(quantity*price)*100.0/(SELECT SUM(quantity*price) FROM sales),2) AS pct\nFROM sales GROUP BY category;"),
    ("Highest-Value Order",                   "SELECT *, (quantity*price) AS order_value FROM sales\nORDER BY order_value DESC LIMIT 1;"),
    ("Average Product Price",                 "SELECT product, ROUND(AVG(price),2) AS avg_price\nFROM sales GROUP BY product ORDER BY avg_price DESC;"),
]

results = [
    "Returns all 30 transaction rows.",
    "Total Revenue = ₹12,92,500",
    "Keyboard — 35 units sold",
    "Pune ₹5,38,500 | Mumbai ₹4,53,500 | Nagpur ₹3,00,500",
    "Electronics 91.3% (₹11,80,000) | Accessories 8.7% (₹1,12,500)",
    "Order #1013 — Laptop, Pune — ₹1,50,000",
    "Laptop ₹50,000 | Mobile ₹20,000 | Headphones ₹2,000 | Keyboard ₹1,500",
]

for i, ((title, sql), result) in enumerate(zip(sql_tasks, results), 1):
    story.append(Paragraph(f"Query {i}: {title}", h2_style))
    story.append(Paragraph(sql, code_style))
    story.append(Paragraph(f"→ Result: {result}", insight_style))
    story.append(Spacer(1, 0.2*cm))

story.append(PageBreak())

# ─────────────────────────────────────────────────────────────
# PAGE 4 – PYTHON ANALYSIS
# ─────────────────────────────────────────────────────────────
story.append(Paragraph("4. Python (Pandas) Analysis", h1_style))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=8))

py_steps = [
    ("Load Dataset",           "df = pd.read_csv('data/sales_data.csv', parse_dates=['order_date'])"),
    ("Display First Rows",     "print(df.head())"),
    ("Dataset Structure",      "df.info()  |  df.describe()"),
    ("Create total_sales",     "df['total_sales'] = df['quantity'] * df['price']"),
    ("Total Revenue",          "total = df['total_sales'].sum()   # ₹12,92,500"),
    ("Most Sold Product",      "df.groupby('product')['quantity'].sum().idxmax()  # Keyboard"),
    ("Group Sales by City",    "df.groupby('city')['total_sales'].sum()"),
    ("Summary Statistics",     "df['total_sales'].describe()"),
]

for step, code in py_steps:
    story.append(Paragraph(step, h2_style))
    story.append(Paragraph(code, code_style))

# Key findings table
story.append(Spacer(1, 0.4*cm))
story.append(Paragraph("Key Findings from Python Analysis", h2_style))
findings_data = [
    ["Metric", "Value"],
    ["Total Revenue",        "₹12,92,500"],
    ["Total Orders",         "30"],
    ["Average Order Value",  "₹43,083.33"],
    ["Most Sold Product",    "Keyboard (35 units)"],
    ["Highest Revenue Product","Laptop (₹7,00,000)"],
    ["Top City",             "Pune (₹5,38,500)"],
    ["Highest Single Order", "₹1,50,000 — Order #1013"],
]
ftbl = Table(findings_data, colWidths=[8*cm, 9*cm])
ftbl.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,0), TABLE_HDR),
    ("TEXTCOLOR",     (0,0), (-1,0), white),
    ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",      (0,0), (-1,-1), 10),
    ("ROWBACKGROUNDS",(0,1), (-1,-1), [white, LIGHT_BG]),
    ("GRID",          (0,0), (-1,-1), 0.4, HexColor("#c0cce0")),
    ("TOPPADDING",    (0,0), (-1,-1), 7),
    ("BOTTOMPADDING", (0,0), (-1,-1), 7),
    ("LEFTPADDING",   (0,0), (-1,-1), 10),
]))
story.append(ftbl)
story.append(PageBreak())

# ─────────────────────────────────────────────────────────────
# PAGE 5 – VISUALIZATIONS
# ─────────────────────────────────────────────────────────────
story.append(Paragraph("5. Visualizations", h1_style))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=8))

charts = [
    ("bar_chart_product_sales.png",    "Bar Chart – Product vs Total Sales Revenue"),
    ("pie_chart_category_sales.png",   "Pie Chart – Category-wise Sales Distribution"),
    ("line_chart_sales_by_date.png",   "Line Chart – Daily Sales Trend"),
    ("grouped_bar_city_product.png",   "Grouped Bar Chart – Product Revenue by City"),
]

for i, (fname, caption) in enumerate(charts):
    fpath = os.path.join(VIZ_DIR, fname)
    if os.path.exists(fpath):
        story.append(Paragraph(f"5.{i+1}  {caption}", h2_style))
        img = Image(fpath, width=15*cm, height=7*cm)
        img.hAlign = "CENTER"
        story.append(img)
        story.append(Spacer(1, 0.4*cm))

story.append(PageBreak())

# ─────────────────────────────────────────────────────────────
# PAGE 6 – EXCEL & TECH STACK
# ─────────────────────────────────────────────────────────────
story.append(Paragraph("6. Excel Analysis", h1_style))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=8))

excel_tasks = [
    "Imported sales_data.csv and created Total Sales column (Quantity × Price)",
    "Sorted products by highest sales value (descending)",
    "Applied city-based filters — separate sheets for Pune, Mumbai, Nagpur",
    "Created Pivot Table: Rows → Product | Columns → City | Values → Total Sales",
    "Identified best product (Laptop) and best city (Pune) from pivot analysis",
    "Summary sheet with 7 KPIs including total revenue, best product, best city",
]
for t in excel_tasks:
    story.append(Paragraph(f"✓  {t}", bullet_style))

story.append(Spacer(1, 0.5*cm))
story.append(Paragraph("Pivot Table Output", h2_style))

pivot_data = [
    ["Product",    "Mumbai",     "Nagpur",     "Pune",       "Grand Total"],
    ["Headphones", "₹10,000",   "₹20,000",   "₹30,000",   "₹60,000"],
    ["Keyboard",   "₹13,500",   "₹10,500",   "₹28,500",   "₹52,500"],
    ["Laptop",     "₹2,00,000", "₹1,50,000", "₹3,50,000", "₹7,00,000"],
    ["Mobile",     "₹2,30,000", "₹1,20,000", "₹1,30,000", "₹4,80,000"],
    ["Grand Total","₹4,53,500", "₹3,00,500", "₹5,38,500", "₹12,92,500"],
]
ptbl = Table(pivot_data, colWidths=[3.5*cm, 3.3*cm, 3.3*cm, 3.3*cm, 3.6*cm])
ptbl.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,0),  TABLE_HDR),
    ("BACKGROUND",    (0,-1),(-1,-1), ACCENT),
    ("TEXTCOLOR",     (0,0), (-1,0),  white),
    ("TEXTCOLOR",     (0,-1),(-1,-1), white),
    ("FONTNAME",      (0,0), (-1,0),  "Helvetica-Bold"),
    ("FONTNAME",      (0,-1),(-1,-1), "Helvetica-Bold"),
    ("FONTSIZE",      (0,0), (-1,-1), 9),
    ("ROWBACKGROUNDS",(0,1), (-1,-2), [white, LIGHT_BG]),
    ("GRID",          (0,0), (-1,-1), 0.4, HexColor("#c0cce0")),
    ("ALIGN",         (1,0), (-1,-1), "CENTER"),
    ("TOPPADDING",    (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ("LEFTPADDING",   (0,0), (-1,-1), 8),
]))
story.append(ptbl)

story.append(Spacer(1, 0.5*cm))
story.append(Paragraph("7. Tech Stack", h1_style))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=8))

tech_data = [
    ["Technology", "Version", "Purpose"],
    ["Python",          "3.10+",   "Core programming language"],
    ["Pandas",          "2.0+",    "Data loading, transformation, analysis"],
    ["NumPy",           "1.24+",   "Numerical computations"],
    ["Matplotlib",      "3.7+",    "Data visualization (bar, pie, line charts)"],
    ["SQLite (stdlib)", "3.x",     "In-memory SQL query execution"],
    ["OpenPyXL",        "3.1+",    "Excel report generation with pivot tables"],
    ["ReportLab",       "4.x",     "PDF documentation generation"],
    ["Git / GitHub",    "Latest",  "Version control & project hosting"],
]
ttbl = Table(tech_data, colWidths=[4*cm, 2.5*cm, 10.5*cm])
ttbl.setStyle(TableStyle([
    ("BACKGROUND",    (0,0), (-1,0), TABLE_HDR),
    ("TEXTCOLOR",     (0,0), (-1,0), white),
    ("FONTNAME",      (0,0), (-1,0), "Helvetica-Bold"),
    ("FONTSIZE",      (0,0), (-1,-1), 9),
    ("ROWBACKGROUNDS",(0,1), (-1,-1), [white, LIGHT_BG]),
    ("GRID",          (0,0), (-1,-1), 0.4, HexColor("#c0cce0")),
    ("TOPPADDING",    (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ("LEFTPADDING",   (0,0), (-1,-1), 8),
]))
story.append(ttbl)
story.append(PageBreak())

# ─────────────────────────────────────────────────────────────
# PAGE 7 – INSIGHTS, FUTURE IMPROVEMENTS, CONCLUSION
# ─────────────────────────────────────────────────────────────
story.append(Paragraph("8. Business Insights & Recommendations", h1_style))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=8))

insights = [
    ("Laptops drive 54.2% of total revenue", "Despite lower unit volume, Laptops generate ₹7L — "
     "the highest of any product. Marketing should protect and grow this segment."),
    ("Pune is the strongest market", "Pune contributes ₹5.38L (41.7%) of all revenue, followed by "
     "Mumbai (₹4.53L) and Nagpur (₹3L). Nagpur has growth potential with targeted campaigns."),
    ("Electronics dominate at 91.3%", "Accessories (Headphones, Keyboard) contribute only 8.7%. "
     "Bundle promotions could lift accessory attachment rates."),
    ("January outperformed February", "January revenue (₹7.71L) was 47.8% higher than February "
     "(₹5.21L). Investigate seasonal patterns and plan inventory accordingly."),
    ("Keyboards are the volume leader", "Keyboards lead in units sold (35) but rank last in revenue "
     "due to low price. Consider upselling premium variants."),
]
for title, detail in insights:
    story.append(Paragraph(f"💡 {title}", h2_style))
    story.append(Paragraph(detail, body_style))

story.append(Spacer(1, 0.4*cm))
story.append(Paragraph("9. Future Improvements", h1_style))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=8))

future = [
    "Integrate a live SQL database (MySQL/PostgreSQL) instead of CSV ingestion",
    "Build an interactive dashboard using Streamlit or Power BI",
    "Add customer segmentation analysis (RFM model)",
    "Implement forecasting with Prophet or ARIMA for sales prediction",
    "Automate pipeline with Apache Airflow for scheduled reporting",
    "Add unit tests with pytest for each analysis module",
]
for f in future:
    story.append(Paragraph(f"→ {f}", bullet_style))

story.append(Spacer(1, 0.4*cm))
story.append(Paragraph("10. Conclusion", h1_style))
story.append(HRFlowable(width="100%", thickness=1, color=ACCENT, spaceAfter=8))
story.append(Paragraph(
    "This capstone project demonstrates a complete, production-grade data analytics pipeline applied to "
    "retail sales data. All required deliverables — SQL queries, Python/Pandas analysis, Excel pivot "
    "reporting, and data visualizations — have been implemented and are version-controlled on GitHub. "
    "The analysis reveals clear strategic priorities: protect the high-revenue Laptop segment, invest "
    "in growing the Nagpur market, and explore accessory bundle strategies to diversify revenue streams.",
    body_style))

story.append(Spacer(1, 0.4*cm))
footer_data = [[Paragraph(
    "Kanhaiya Thakur  |  Data Engineering Capstone  |  April 2026  |  github.com/Kanhaiyathakur001",
    S("FT", fontSize=8, fontName="Helvetica", textColor=white, alignment=TA_CENTER))]]
footer_tbl = Table(footer_data, colWidths=[17*cm])
footer_tbl.setStyle(TableStyle([
    ("BACKGROUND", (0,0),(-1,-1), BLUE),
    ("TOPPADDING",    (0,0),(-1,-1), 10),
    ("BOTTOMPADDING", (0,0),(-1,-1), 10),
]))
story.append(footer_tbl)

# ─── Build ──────────────────────────────────────────────────
doc.build(story)
print(f"✅ PDF documentation saved: {OUTPUT}")
