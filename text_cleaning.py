import pandas as pd

# Load the raw customer dataset
df = pd.read_csv("customer_dataset.csv")

# Clean customer names: normalize multiple spaces, remove leading/trailing spaces, and use proper case
df["Customer_Name"] = (
    df["Customer_Name"]
    .str.replace(r"\\s+", " ", regex=True)
    .str.strip()
    .str.title()
)

# Clean emails: remove extra spaces and standardize to lowercase
df["Email"] = df["Email"].str.strip().str.lower()

# Clean city names
df["City"] = (
    df["City"]
    .str.replace(r"\\s+", " ", regex=True)
    .str.strip()
    .str.title()
)

# Clean status values
df["Status"] = df["Status"].str.strip().str.lower().str.title()

# Save cleaned dataset
df.to_csv("cleaned_customer_dataset.csv", index=False)

print("Text cleaning completed successfully.")
print(df)
