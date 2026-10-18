-- ============================================
-- 01. DATA CLEANING
-- E-Commerce Sales Dataset
-- ============================================

-- Create a cleaned view / table
CREATE OR REPLACE VIEW orders_clean AS
SELECT
    Order_ID,
    CAST(Order_Date AS DATE) AS order_date,
    Customer_ID,
    Customer_Name,
    Category,
    Product,
    Region,
    COALESCE(City, 'Unknown') AS City,
    Quantity,
    Unit_Price,
    COALESCE(Discount, 0) AS Discount,
    COALESCE(Payment_Method, 'Unknown') AS Payment_Method,
    Shipping_Cost,
    Order_Status,
    -- Calculated revenue (after discount)
    ROUND(Quantity * Unit_Price * (1 - COALESCE(Discount, 0)), 2) AS Revenue,
    EXTRACT(YEAR FROM CAST(Order_Date AS DATE)) AS order_year,
    EXTRACT(MONTH FROM CAST(Order_Date AS DATE)) AS order_month
FROM orders
WHERE Quantity > 0 AND Unit_Price > 0;

-- Quick check of nulls after cleaning
SELECT
    COUNT(*) AS total_rows,
    COUNT(*) FILTER (WHERE City = 'Unknown') AS unknown_city,
    COUNT(*) FILTER (WHERE Payment_Method = 'Unknown') AS unknown_payment
FROM orders_clean;
