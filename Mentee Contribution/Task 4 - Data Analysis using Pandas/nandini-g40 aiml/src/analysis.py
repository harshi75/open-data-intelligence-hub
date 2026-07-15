import pandas as pd
import os

# Load dataset
df = pd.read_csv("data/supersale_.csv")

# Create outputs folder
os.makedirs("outputs", exist_ok=True)

# Basic info
print(df.head())
print(df.info())

# Cleaning example
df.drop_duplicates(inplace=True)

# Save cleaned dataset
df.to_csv("outputs/cleaned_dataset.csv", index=False)

# Excel export
df.to_excel("outputs/cleaned_dataset.xlsx", index=False)

# Category summary
category_summary = df.groupby("Category").agg(
    total_sales=("Sales", "sum")
).reset_index()

category_summary.to_csv("outputs/category_summary.csv", index=False)

print("Analysis completed successfully!")