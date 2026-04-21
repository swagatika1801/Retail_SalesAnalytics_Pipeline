-- ============================================================
-- Retail Store Sales Analysis - SQL Queries
-- Author: Kanhaiya Thakur
-- Dataset: sales_data.csv (imported into SQLite/MySQL)
-- ============================================================

-- --------------------------------------------------------
-- SETUP: Create Table
-- --------------------------------------------------------
CREATE TABLE IF NOT EXISTS sales (
    order_id    INTEGER PRIMARY KEY,
    order_date  DATE,
    city        VARCHAR(50),
    product     VARCHAR(100),
    category    VARCHAR(50),
    quantity    INTEGER,
    price       DECIMAL(10,2)
);

-- --------------------------------------------------------
-- QUERY 1: Display All Sales Records
-- --------------------------------------------------------
SELECT * FROM sales;

-- --------------------------------------------------------
-- QUERY 2: Calculate Total Sales Revenue
-- --------------------------------------------------------
SELECT 
    ROUND(SUM(quantity * price), 2) AS total_revenue
FROM sales;

-- --------------------------------------------------------
-- QUERY 3: Top-Selling Product by Quantity
-- --------------------------------------------------------
SELECT 
    product,
    SUM(quantity) AS total_quantity_sold
FROM sales
GROUP BY product
ORDER BY total_quantity_sold DESC
LIMIT 1;

-- --------------------------------------------------------
-- QUERY 4: Total Revenue Generated in Each City
-- --------------------------------------------------------
SELECT 
    city,
    ROUND(SUM(quantity * price), 2) AS city_revenue
FROM sales
GROUP BY city
ORDER BY city_revenue DESC;

-- --------------------------------------------------------
-- QUERY 5: Category-Wise Revenue
-- --------------------------------------------------------
SELECT 
    category,
    ROUND(SUM(quantity * price), 2) AS category_revenue,
    ROUND(SUM(quantity * price) * 100.0 / (SELECT SUM(quantity * price) FROM sales), 2) AS revenue_percentage
FROM sales
GROUP BY category
ORDER BY category_revenue DESC;

-- --------------------------------------------------------
-- QUERY 6: Highest-Value Order
-- --------------------------------------------------------
SELECT 
    order_id,
    order_date,
    city,
    product,
    quantity,
    price,
    (quantity * price) AS order_value
FROM sales
ORDER BY order_value DESC
LIMIT 1;

-- --------------------------------------------------------
-- QUERY 7: Average Product Price
-- --------------------------------------------------------
SELECT 
    product,
    ROUND(AVG(price), 2) AS avg_price
FROM sales
GROUP BY product
ORDER BY avg_price DESC;

-- --------------------------------------------------------
-- BONUS QUERIES
-- --------------------------------------------------------

-- Monthly Revenue Trend
SELECT 
    strftime('%Y-%m', order_date) AS month,
    ROUND(SUM(quantity * price), 2) AS monthly_revenue
FROM sales
GROUP BY month
ORDER BY month;

-- Top 3 Products by Revenue
SELECT 
    product,
    ROUND(SUM(quantity * price), 2) AS total_revenue
FROM sales
GROUP BY product
ORDER BY total_revenue DESC
LIMIT 3;

-- City + Product Revenue Matrix
SELECT 
    city,
    product,
    ROUND(SUM(quantity * price), 2) AS revenue
FROM sales
GROUP BY city, product
ORDER BY city, revenue DESC;
