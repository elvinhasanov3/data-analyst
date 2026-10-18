# 📈 Sales Performance Dashboard (Power BI)

**Goal:** Give executives a single interactive view of sales, profit, and customer trends with filters for region, category, and time.

**Stack:** Power BI · DAX · Power Query

**Data:** Real Azerbaijan E-Commerce dataset (`ecommerce_sales_dataset.csv` – 15,025 orders)

---

## 📌 What the dashboard answers

- How are we performing overall? (Revenue, Orders, AOV, Completion Rate)
- Which regions and categories drive the most revenue?
- What is the monthly trend?
- Order status breakdown (Completed / Cancelled / Returned)
- Payment method mix

---

## 📂 Project Structure

```
03-powerbi-dashboard/
├── data/
│   └── ecommerce_sales_dataset.csv
├── screenshots/              ← Add dashboard images
│   ├── overview.png
│   ├── by_region.png
│   └── by_product.png
├── Sales_Dashboard.pbix      ← Build and add the file
└── README.md
```

---

## 🛠️ Key Features to Build

- **KPI cards**: Total Revenue (Completed), Orders, Avg Order Value, Completion Rate %
- **Time intelligence**: Monthly trend
- **Interactive filters**: Region, Category, Order Status, Date
- **Visuals**: Bar charts by Category/Region, Donut for Status, Line for trend

---

## 📊 Sample DAX Measures

```dax
Revenue = SUMX('orders', [Quantity] * [Unit_Price] * (1 - COALESCE([Discount], 0)))

Completed Revenue = CALCULATE([Revenue], 'orders'[Order_Status] = "Completed")

Completion Rate = DIVIDE(
    CALCULATE(COUNTROWS('orders'), 'orders'[Order_Status] = "Completed"),
    COUNTROWS('orders')
)
```

---

## 🔍 Key Insights from the Data

- Electronics ≈ 56% of completed revenue
- Baku ≈ 42% of revenue
- Card is the top payment method (51.5%)
- Cancellation rate highest in Electronics (~6.6%)

---

## 💡 Recommendation example

Focus growth efforts on under-indexed regions (Lankaran, Shaki-Zagatala) while protecting the high-performing Electronics category and investigating its slightly higher cancellation rate.
