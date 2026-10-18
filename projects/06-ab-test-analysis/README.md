# 🧪 A/B Test Analysis – Discount Strategy Impact

**Goal:** Evaluate whether offering a higher discount (Test group) improves conversion and revenue compared to the current discount levels (Control), using statistical testing.

**Stack:** Python · pandas · scipy / statsmodels · matplotlib / seaborn

**Data:** `ecommerce_sales_dataset.csv` + simulated experiment assignment

---

## 📌 Experiment Design

**Hypothesis:**  
Increasing the average discount from ~5.6% to ~12% will increase order completion rate and total revenue per visitor.

**Groups (simulated for portfolio):**
- **Control** – current discount distribution (actual data)
- **Test** – higher discount applied to a random 50% of orders (simulated)

**Primary metrics:**
1. Completion Rate (Completed / Total orders)
2. Average Revenue per Order (Completed)
3. Total Revenue

**Secondary:** Cancellation rate, Average Order Value

---

## 📂 Project Structure

```
06-ab-test-analysis/
├── data/
│   └── ecommerce_sales_dataset.csv
├── notebooks/
│   └── ab_test_analysis.ipynb      ← Main analysis notebook
├── scripts/
│   └── ab_test_pipeline.py
├── outputs/
│   ├── results_summary.csv
│   └── charts/
└── README.md
```

---

## 🔍 Method

1. Load the real orders dataset
2. Randomly assign each order to Control or Test (seed fixed for reproducibility)
3. For Test group, simulate a higher discount (e.g. +6 percentage points, capped at 20%)
4. Recalculate Revenue under the new discount
5. Compare:
   - Completion rate (Chi-square or proportion z-test)
   - Mean revenue (t-test or Mann-Whitney)
6. Report lift, p-value, confidence intervals, and practical significance

---

## 📊 Expected Output Structure (fill with your results)

| Metric                  | Control     | Test        | Lift    | p-value | Significant? |
|-------------------------|-------------|-------------|---------|---------|--------------|
| Completion Rate         | 84.6%       | 84.4%       | -0.3%   | 0.713   | No            |
| Avg Revenue / Order     | 473.9 AZN   | 475.0 AZN   | +0.2%   | 0.931   | No            |
| Total Revenue (sample)  | x.xxM       | x.xxM       | +x.x%   | —       | —            |

---

## ▶️ How to run

```bash
cd 06-ab-test-analysis
pip install -r requirements.txt
python scripts/ab_test_pipeline.py
# or open the notebook
jupyter notebook notebooks/ab_test_analysis.ipynb
```

---

## 💡 Business Recommendation Framework

- If **statistically significant positive lift** and practical effect size is meaningful → recommend rolling out the higher discount (or a refined version).
- If **no significant difference** → keep current discount strategy; the extra discount cost is not justified.
- Always check **guardrail metrics** (cancellation rate, margin impact).

> Note: This is a portfolio simulation. In a real experiment you would randomize at user/session level before the order is placed and track the full funnel.
