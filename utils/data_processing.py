import pandas as pd

def process_vehicle_data(df):
    if df.empty:
        return df
        
    pivot_df = df.pivot(index=["Camera", "Data/Hora"], columns="Type", values="Count").fillna(0).reset_index()
    pivot_df["Total"] = pivot_df["C1"] + pivot_df["C2"] + pivot_df["C3"]
    pivot_df["Acumulado"] = pivot_df["Total"].rolling(window=4, min_periods=1).sum()

    pivot_df["Data/Hora"] = pd.to_datetime(pivot_df["Data/Hora"]).dt.strftime("%Y-%m-%d %H:%M:%S")

    return pivot_df