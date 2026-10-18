"""
A/B Test Pipeline – Discount Strategy
Simulates Control vs Test groups on the real e-commerce dataset.
"""

import pandas as pd
import numpy as np
from scipy import stats

def load_and_prepare(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    df["Discount"] = df["Discount"].fillna(0)
    df["Revenue"] = df["Quantity"] * df["Unit_Price"] * (1 - df["Discount"])
    df["Completed"] = (df["Order_Status"] == "Completed").astype(int)
    return df

def assign_groups(df: pd.DataFrame, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    df = df.copy()
    df["Group"] = rng.choice(["Control", "Test"], size=len(df), p=[0.5, 0.5])
    return df

def apply_test_discount(df: pd.DataFrame, extra_discount: float = 0.06) -> pd.DataFrame:
    """Simulate higher discount for Test group and recalculate revenue."""
    df = df.copy()
    df["Sim_Discount"] = df["Discount"]
    mask = df["Group"] == "Test"
    df.loc[mask, "Sim_Discount"] = np.minimum(df.loc[mask, "Discount"] + extra_discount, 0.20)
    df["Sim_Revenue"] = df["Quantity"] * df["Unit_Price"] * (1 - df["Sim_Discount"])
    return df

def proportion_test(control: pd.Series, test: pd.Series):
    """Two-proportion z-test for completion rate."""
    n1, n2 = len(control), len(test)
    p1, p2 = control.mean(), test.mean()
    p_pool = (control.sum() + test.sum()) / (n1 + n2)
    se = np.sqrt(p_pool * (1 - p_pool) * (1/n1 + 1/n2))
    z = (p2 - p1) / se
    p_value = 2 * (1 - stats.norm.cdf(abs(z)))
    return p1, p2, z, p_value

def run_ab_test(data_path: str):
    df = load_and_prepare(data_path)
    df = assign_groups(df)
    df = apply_test_discount(df)

    control = df[df["Group"] == "Control"]
    test = df[df["Group"] == "Test"]

    # Completion rate
    p_c, p_t, z, p_val = proportion_test(control["Completed"], test["Completed"])
    print("=== Completion Rate ===")
    print(f"Control: {p_c:.1%}  |  Test: {p_t:.1%}  |  Lift: {(p_t-p_c)/p_c:.1%}")
    print(f"z = {z:.3f}, p-value = {p_val:.4f}")

    # Revenue (Completed only)
    rev_c = control.loc[control["Completed"]==1, "Revenue"]
    rev_t = test.loc[test["Completed"]==1, "Sim_Revenue"]
    t_stat, p_rev = stats.ttest_ind(rev_c, rev_t, equal_var=False)
    print("\n=== Avg Revenue per Completed Order ===")
    print(f"Control: {rev_c.mean():.2f}  |  Test: {rev_t.mean():.2f}  |  Lift: {(rev_t.mean()-rev_c.mean())/rev_c.mean():.1%}")
    print(f"t = {t_stat:.3f}, p-value = {p_rev:.4f}")

    # Summary table
    summary = pd.DataFrame({
        "Metric": ["Completion Rate", "Avg Revenue (Completed)", "Sample Size"],
        "Control": [f"{p_c:.1%}", f"{rev_c.mean():.2f}", len(control)],
        "Test": [f"{p_t:.1%}", f"{rev_t.mean():.2f}", len(test)],
        "Lift": [f"{(p_t-p_c)/p_c:.1%}", f"{(rev_t.mean()-rev_c.mean())/rev_c.mean():.1%}", "-"],
        "p-value": [f"{p_val:.4f}", f"{p_rev:.4f}", "-"]
    })
    print("\n", summary.to_string(index=False))
    summary.to_csv("outputs/results_summary.csv", index=False)
    print("\nResults saved to outputs/results_summary.csv")
    return df, summary

if __name__ == "__main__":
    run_ab_test("data/ecommerce_sales_dataset.csv")
