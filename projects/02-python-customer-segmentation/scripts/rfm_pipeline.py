"""
RFM Customer Segmentation Pipeline
Replace the sample data loading with your real dataset.
"""

import pandas as pd
import numpy as np
from datetime import datetime

def load_data(path: str) -> pd.DataFrame:
    """Load and basic clean of transaction data."""
    df = pd.read_csv(path, parse_dates=["order_date"])
    df = df.dropna(subset=["customer_id", "order_date", "sales"])
    return df

def calculate_rfm(df: pd.DataFrame, analysis_date: datetime = None) -> pd.DataFrame:
    """Calculate Recency, Frequency, Monetary for each customer."""
    if analysis_date is None:
        analysis_date = df["order_date"].max() + pd.Timedelta(days=1)

    rfm = df.groupby("customer_id").agg(
        recency=("order_date", lambda x: (analysis_date - x.max()).days),
        frequency=("order_id", "nunique"),
        monetary=("sales", "sum")
    ).reset_index()

    return rfm

def score_rfm(rfm: pd.DataFrame) -> pd.DataFrame:
    """Assign 1-5 scores (5 = best)."""
    rfm = rfm.copy()

    # Recency: lower is better → reverse
    rfm["R"] = pd.qcut(rfm["recency"], 5, labels=[5, 4, 3, 2, 1]).astype(int)
    rfm["F"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1, 2, 3, 4, 5]).astype(int)
    rfm["M"] = pd.qcut(rfm["monetary"], 5, labels=[1, 2, 3, 4, 5]).astype(int)

    rfm["RFM_Score"] = rfm["R"].astype(str) + rfm["F"].astype(str) + rfm["M"].astype(str)
    return rfm

def assign_segment(row) -> str:
    """Simple segment rules based on R and F scores."""
    r, f = row["R"], row["F"]
    if r >= 4 and f >= 4:
        return "Champions"
    elif r >= 3 and f >= 3:
        return "Loyal Customers"
    elif r >= 4 and f <= 2:
        return "New Customers"
    elif r <= 2 and f >= 3:
        return "At Risk"
    elif r <= 2 and f <= 2:
        return "Hibernating"
    else:
        return "Potential Loyalists"

def run_pipeline(data_path: str, output_path: str = "outputs/segments_summary.csv"):
    df = load_data(data_path)
    rfm = calculate_rfm(df)
    rfm = score_rfm(rfm)
    rfm["Segment"] = rfm.apply(assign_segment, axis=1)

    summary = rfm.groupby("Segment").agg(
        customers=("customer_id", "count"),
        avg_recency=("recency", "mean"),
        avg_frequency=("frequency", "mean"),
        total_monetary=("monetary", "sum")
    ).round(2)

    print(summary)
    rfm.to_csv(output_path, index=False)
    print(f"\nSegments saved to {output_path}")
    return rfm

if __name__ == "__main__":
    # Example usage – replace with your file
    # run_pipeline("data/raw/transactions.csv")
    print("RFM pipeline ready. Uncomment and provide your data path.")
