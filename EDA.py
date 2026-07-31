import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
rotation=(45)
import pandas as pd

# Load dataset
df = pd.read_excel("global_superstore_2016.xlsx")

# First 5 rows
print(df.head())

# Number of rows and columns
print("\nShape of Dataset:")
print(df.shape)

# Column names
print("\nColumns:")
print(df.columns)

# Data types
print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

print("\nSummary Statistics:")
print(df.describe())


import matplotlib.pyplot as plt

sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))
sales.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.tight_layout()
plt.savefig("sales_by_category.png")
plt.show()


profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8,5))
profit.plot(kind="bar", color="green")

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")

plt.tight_layout()
plt.savefig("profit_by_category.png")
plt.show()


plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.show()
# Load the dataset
df = pd.read_excel("global_superstore_2016.xlsx")

# Profit by Category
profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8,5))
profit.plot(kind="bar", color="green")

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")

plt.tight_layout()
plt.savefig("profit_by_category.png")
plt.show()

# Sales by Region

region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(10,5))
region_sales.plot(kind="bar", color="orange")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("sales_by_region.png")
plt.show()


# Sales by Customer Segment

segment_sales = df.groupby("Segment")["Sales"].sum()

plt.figure(figsize=(7,7))

plt.pie(
    segment_sales,
    labels=segment_sales.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Sales by Customer Segment")

plt.tight_layout()
plt.savefig("sales_by_segment.png")
plt.show()

# Profit by Sub-Category

subcategory_profit = df.groupby("Sub-Category")["Profit"].sum().sort_values()

plt.figure(figsize=(12,8))

subcategory_profit.plot(kind="barh", color="purple")

plt.title("Profit by Sub-Category")
plt.xlabel("Profit")
plt.ylabel("Sub-Category")

plt.tight_layout()
plt.savefig("profit_by_subcategory.png")
plt.show()

# Discount vs Profit

plt.figure(figsize=(8,6))

plt.scatter(
    df["Discount"],
    df["Profit"],
    alpha=0.5,
    color="red"
)

plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")

plt.grid(True)

plt.tight_layout()
plt.savefig("discount_vs_profit.png")
plt.show()

print("\n========== KEY INSIGHTS ==========")

print("\nHighest Sales Category:")
print(df.groupby("Category")["Sales"].sum().idxmax())

print("\nHighest Profit Category:")
print(df.groupby("Category")["Profit"].sum().idxmax())

print("\nHighest Sales Region:")
print(df.groupby("Region")["Sales"].sum().idxmax())

print("\nHighest Sales Segment:")
print(df.groupby("Segment")["Sales"].sum().idxmax())

print("\nLeast Profitable Sub-Category:")
print(df.groupby("Sub-Category")["Profit"].sum().idxmin())

