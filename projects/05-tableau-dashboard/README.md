# 📊 E-Commerce Dashboard (Tableau)

**Goal:** Build an interactive executive dashboard that answers “How is the business performing?” in under 10 seconds.

**Stack:** Tableau Desktop / Tableau Public · calculated fields · parameters · filters

**Data:** Same `ecommerce_sales_dataset.csv` (15,025 orders, 2025)

---

## 📌 Dashboard Questions

- Total Revenue, Orders, AOV, and Completion Rate (KPIs)
- Revenue by Category and Region (bar / map)
- Monthly trend with year-over-year style comparison
- Order Status breakdown (Completed / Cancelled / Returned / Pending)
- Top Products and Payment Method mix
- Discount vs Revenue relationship

---

## 📂 Project Structure

```
05-tableau-dashboard/
├── data/
│   └── ecommerce_sales_dataset.csv
├── screenshots/                  ← Add your dashboard images here
│   ├── overview.png
│   ├── by_region.png
│   └── trend.png
├── Azerbaijan_Ecommerce_Dashboard.twbx   ← Publish & add the file
└── README.md
```

---

## 🛠️ Recommended Sheets & Dashboard Layout

1. **KPI Row**  
   - Total Revenue (Completed)  
   - Total Orders  
   - Average Order Value  
   - Completion Rate %

2. **Category Performance** (horizontal bar)  
   - Color by Category, size/label by Revenue

3. **Region Performance** (map or bar)  
   - Use Region field; highlight Baku vs others

4. **Monthly Trend** (line + dual axis for orders)  
   - Order_Date continuous

5. **Order Status Donut / Stacked Bar**

6. **Filters** (always visible)  
   - Region, Category, Order Status, Date range

---

## 📐 Key Calculated Fields (Tableau)

```
// Revenue
[Quantity] * [Unit_Price] * (1 - ZN([Discount]))

// Completion Rate
SUM(IF [Order_Status] = "Completed" THEN 1 END) / COUNT([Order_ID])

// Month
DATETRUNC('month', [Order_Date])
```

---

## 🔍 Insights to Highlight on the Dashboard

- Electronics ≈ **56%** of completed revenue
- Baku alone ≈ **42%** of revenue
- Cancellation rate highest in Electronics (~6.6%)
- Card is the dominant payment method (51.5%)
- Revenue relatively stable month-to-month with mild peaks in May, Aug, Dec

---

## 💡 How to publish

1. Open Tableau → Connect to the CSV
2. Build the sheets and one clean dashboard
3. Save as `.twbx` (packaged workbook)
4. Publish to Tableau Public and put the public link in this README
5. Export 2–3 screenshots into the `screenshots/` folder

**Live link (add yours):**  
[Your Tableau Public URL here]
