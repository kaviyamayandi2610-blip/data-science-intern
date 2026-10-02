import pandas as pd
import os

# ============================================================
# 1. LOAD THE RAW DATASET
# ============================================================

input_file = r"C:\Users\KAVIYA M\OneDrive\Desktop\task 1\raw_data.csv"
output_file = r"C:\Users\KAVIYA M\OneDrive\Desktop\task 1\output\cleaned_sales_data.csv"
df = pd.read_csv(input_file)

print("=" * 60)
print("DATA CLEANING AND PREPROCESSING")
print("=" * 60)

print("\nOriginal Dataset:")
print(df)

print("\nOriginal Shape:")
print(df.shape)


# ============================================================
# 2. CHECK MISSING VALUES
# ============================================================

print("\n" + "=" * 60)
print("MISSING VALUES BEFORE CLEANING")
print("=" * 60)

print(df.isnull().sum())


# ============================================================
# 3. CLEAN COLUMN NAMES
# ============================================================

df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("\nCleaned Column Names:")
print(df.columns.tolist())


# ============================================================
# 4. REMOVE DUPLICATE RECORDS
# ============================================================

duplicates = df.duplicated().sum()

print("\nNumber of Duplicate Rows:", duplicates)

df = df.drop_duplicates()

print("Duplicate rows removed.")


# ============================================================
# 5. STANDARDIZE GENDER VALUES
# ============================================================

df["gender"] = df["gender"].replace({
    "M": "Male",
    "F": "Female"
})

df["gender"] = df["gender"].str.strip().str.title()


# ============================================================
# 6. STANDARDIZE COUNTRY VALUES
# ============================================================

df["country"] = df["country"].str.strip().str.title()


# ============================================================
# 7. HANDLE MISSING VALUES
# ============================================================

# Quantity → fill missing value with median
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")

df["quantity"] = df["quantity"].fillna(
    df["quantity"].median()
)

# Sales → fill missing value with median
df["sales"] = pd.to_numeric(df["sales"], errors="coerce")

df["sales"] = df["sales"].fillna(
    df["sales"].median()
)

# Profit → convert to numeric
df["profit"] = pd.to_numeric(
    df["profit"],
    errors="coerce"
)

# Fill missing customer names
df["customer_name"] = df["customer_name"].fillna("Unknown")

# Fill missing dates
df["order_date"] = df["order_date"].fillna("Unknown")


# ============================================================
# 8. STANDARDIZE DATE FORMAT
# ============================================================

# Convert valid dates into datetime
df["order_date"] = pd.to_datetime(
    df["order_date"],
    errors="coerce",
    dayfirst=True
)

# Fill invalid/missing dates using the most common date
if df["order_date"].isnull().sum() > 0:
    most_common_date = df["order_date"].mode()[0]
    df["order_date"] = df["order_date"].fillna(
        most_common_date
    )

# Convert date to DD-MM-YYYY format
df["order_date"] = df["order_date"].dt.strftime("%d-%m-%Y")


# ============================================================
# 9. CHECK AND FIX DATA TYPES
# ============================================================

df["order_id"] = pd.to_numeric(
    df["order_id"],
    errors="coerce"
).astype("Int64")

df["quantity"] = pd.to_numeric(
    df["quantity"],
    errors="coerce"
).astype("Int64")

df["sales"] = pd.to_numeric(
    df["sales"],
    errors="coerce"
)

df["profit"] = pd.to_numeric(
    df["profit"],
    errors="coerce"
)


# ============================================================
# 10. REMOVE EXTRA SPACES FROM TEXT COLUMNS
# ============================================================

text_columns = [
    "customer_name",
    "gender",
    "country",
    "product",
    "category"
]

for column in text_columns:
    df[column] = df[column].astype(str).str.strip()


# ============================================================
# 11. FINAL MISSING VALUE CHECK
# ============================================================

print("\n" + "=" * 60)
print("MISSING VALUES AFTER CLEANING")
print("=" * 60)

print(df.isnull().sum())


# ============================================================
# 12. FINAL DUPLICATE CHECK
# ============================================================

print("\n" + "=" * 60)
print("DUPLICATES AFTER CLEANING")
print("=" * 60)

print("Duplicate rows:", df.duplicated().sum())


# ============================================================
# 13. FINAL DATA TYPES
# ============================================================

print("\n" + "=" * 60)
print("FINAL DATA TYPES")
print("=" * 60)

print(df.dtypes)


# ============================================================
# 14. SAVE CLEANED DATASET
# ============================================================

os.makedirs("output", exist_ok=True)

df.to_csv(
    output_file,
    index=False
)


# ============================================================
# 15. DISPLAY CLEANED DATASET
# ============================================================

print("\n" + "=" * 60)
print("CLEANED DATASET")
print("=" * 60)

print(df)

print("\nFinal Shape:")
print(df.shape)

print("\nCleaned dataset saved successfully!")
print("File:", output_file)

print("\n" + "=" * 60)
print("DATA CLEANING COMPLETED")
print("=" * 60)