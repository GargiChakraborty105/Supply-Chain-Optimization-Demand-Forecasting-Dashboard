import pandas as pd
import numpy as np

# Load the provided CSV file
df = pd.read_csv("supply_chain_sample_data.csv")

# Add 'Lead_Time' column with random values between 3 and 14 days
df["Lead_Time"] = np.random.randint(3, 15, size=len(df))

# Add 'Supplier_Reliability' column with random reliability percentages between 70% and 99%
df["Supplier_Reliability"] = np.random.uniform(70, 99, size=len(df)).round(2)

# Save the updated dataset to a new CSV file
df.to_csv("supply_chain_updated_data.csv", index=False)
