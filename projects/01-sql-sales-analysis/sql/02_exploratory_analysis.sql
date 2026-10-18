-- ============================================
-- 02. EXPLORATORY DATA ANALYSIS
-- ============================================

-- Overall KPIs
SELECT
    COUNT(*) AS total_orders,
    COUNT(*) FILTER (WHERE Order_Status = 'Completed') AS completed_orders,
    ROUND(SUM(Revenue), 2) AS total_revenue,
    ROUND(SUM(Revenue) FILTER (WHERE Order_Status = 'Completed'), 2) AS completed_revenue,
    ROUND(AVG(Revenue), 2) AS avg_order_value
FROM orders_clean;

-- Order Status breakdown
SELECT
    Order_Status,
    COUNT(*) AS orders,
    ROUND(COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 1) AS pct,
    ROUND(SUM(Revenue), 2) AS revenue
FROM orders_clean
GROUP BY Order_Status
ORDER BY orders DESC;

-- Category performance
SELECT
    Category,
    COUNT(*) AS orders,
    ROUND(SUM(Revenue), 2) AS revenue,
    ROUND(AVG(Discount), 3) AS avg_discount
FROM orders_clean
WHERE Order_Status = 'Completed'
GROUP BY Category
ORDER BY revenue DESC;

-- Region performance
SELECT
    Region,
    COUNT(*) AS orders,
    ROUND(SUM(Revenue), 2) AS revenue
FROM orders_clean
WHERE Order_Status = 'Completed'
GROUP BY Region
ORDER BY revenue DESC;
