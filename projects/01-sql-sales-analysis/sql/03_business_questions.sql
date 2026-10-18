-- ============================================
-- 03. BUSINESS QUESTIONS
-- ============================================

-- Q1: Top 10 products by revenue (Completed)
SELECT
    Product,
    Category,
    COUNT(*) AS orders,
    ROUND(SUM(Revenue), 2) AS revenue
FROM orders_clean
WHERE Order_Status = 'Completed'
GROUP BY Product, Category
ORDER BY revenue DESC
LIMIT 10;

-- Q2: Cancellation rate by Category
SELECT
    Category,
    COUNT(*) AS total_orders,
    COUNT(*) FILTER (WHERE Order_Status = 'Cancelled') AS cancelled,
    ROUND(COUNT(*) FILTER (WHERE Order_Status = 'Cancelled') * 100.0 / COUNT(*), 1) AS cancel_rate_pct
FROM orders_clean
GROUP BY Category
ORDER BY cancel_rate_pct DESC;

-- Q3: Monthly sales trend (Completed)
SELECT
    order_year,
    order_month,
    COUNT(*) AS orders,
    ROUND(SUM(Revenue), 2) AS monthly_revenue
FROM orders_clean
WHERE Order_Status = 'Completed'
GROUP BY order_year, order_month
ORDER BY order_year, order_month;

-- Q4: Payment method distribution
SELECT
    Payment_Method,
    COUNT(*) AS orders,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 1) AS pct,
    ROUND(SUM(Revenue), 2) AS revenue
FROM orders_clean
WHERE Order_Status = 'Completed'
GROUP BY Payment_Method
ORDER BY orders DESC;

-- Q5: Discount impact – average revenue by discount bucket
SELECT
    CASE
        WHEN Discount = 0 THEN '0%'
        WHEN Discount <= 0.05 THEN '1-5%'
        WHEN Discount <= 0.10 THEN '6-10%'
        WHEN Discount <= 0.15 THEN '11-15%'
        ELSE '16%+'
    END AS discount_bucket,
    COUNT(*) AS orders,
    ROUND(AVG(Revenue), 2) AS avg_revenue,
    ROUND(SUM(Revenue), 2) AS total_revenue
FROM orders_clean
WHERE Order_Status = 'Completed'
GROUP BY 1
ORDER BY 1;
