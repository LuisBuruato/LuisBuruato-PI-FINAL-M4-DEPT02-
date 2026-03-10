import pandas as pd

df = pd.read_csv("data/raw/data.csv")

df["amount"] = df["value"] * 1.1

df.to_parquet("data/gold/data.parquet")

print("Datos guardados en Gold en formato Parquet")