# 🛒 E-Commerce Sales Analysis (SQL)

**Goal:** Analyze real e-commerce orders from Azerbaijan (2025) to answer key business questions about revenue, categories, regions, discounts, and order status.

**Stack:** SQL (PostgreSQL / SQLite / DuckDB) · CTEs · Window Functions · Aggregations

**Data:** `ecommerce_sales_dataset.csv` — **15,025 orders** (Jan–Dec 2025)

---

## 📌 Business Questions Answered

1. What is the total revenue and how is it distributed by Category and Region?
2. Which products and categories drive the most revenue?
3. What is the cancellation / return rate and where is it highest?
4. How do discounts affect order volume and revenue?
5. What is the monthly sales trend and seasonality?
6. Which payment methods are most used?

---

## 📂 Project Structure

```
01-sql-sales-analysis/
├── data/
│   └── ecommerce_sales_dataset.csv   ← Real dataset (15k rows)
├── sql/
│   ├── 01_data_cleaning.sql
│   ├── 02_exploratory_analysis.sql
│   └── 03_business_questions.sql
├── outputs/
└── README.md
```

---

## 🧹 Data Notes & Cleaning

- **15,025** total orders
- Date range: **2025-01-01 → 2025-12-31**
- Missing values: ~40 rows have nulls in `City`, `Discount`, `Payment_Method` (handled)
- Order Status: Completed (84.5%), Cancelled (6.0%), Returned (5.9%), Pending (3.7%)
- Calculated field: `Revenue = Quantity * Unit_Price * (1 - Discount)`

---

## 🔍 Key Findings (from real data)

| Metric | Value |
|--------|-------|
| Total Revenue (all orders) | ≈ **7.42M AZN** |
| Completed Revenue | ≈ **6.21M AZN** |
| Top Category | **Electronics** (≈ 56% of completed revenue) |
| Top Region | **Baku** (≈ 42% of completed revenue) |
| Most used Payment | **Card** (51.5%) |
| Avg Discount | ~5.6% across categories |
| Highest Cancel Rate | Electronics (6.6%) |

**Monthly insight:** Revenue is relatively stable, with peaks in May, August and December.

---

## ▶️ How to run

1. Load the CSV into your database (PostgreSQL example):
   ```sql
   CREATE TABLE orders (
       Order_ID TEXT,
       Order_Date DATE,
       Customer_ID INT,
       Customer_Name TEXT,
       Category TEXT,
       Product TEXT,
       Region TEXT,
       City TEXT,
       Quantity INT,
       Unit_Price NUMERIC,
       Discount NUMERIC,
       Payment_Method TEXT,
       Shipping_Cost NUMERIC,
       Order_Status TEXT
   );
   -- then COPY or import the CSV
   ```
2. Run the scripts in order:
   ```sql
   \i sql/01_data_cleaning.sql
   \i sql/02_exploratory_analysis.sql
   \i sql/03_business_questions.sql
   ```

---

## 💡 Recommendations

1. **Focus on Electronics** — it drives the majority of revenue; investigate the slightly higher cancellation rate.
2. **Baku & Absheron** dominate sales — consider targeted campaigns in other regions (Ganja-Gazakh, Lankaran) to grow.
3. **Card is king** — optimize the card checkout experience; Digital Wallet has room to grow.
4. Monitor **Returned** orders (almost as high as Cancelled) — dig into product quality or shipping issues.
