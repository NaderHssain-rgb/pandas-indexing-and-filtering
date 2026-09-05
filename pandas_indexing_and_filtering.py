import pandas as pd

# Read Excel file
df = pd.read_excel("Employee.xlsx")

# Select a value by position
print(df.iloc[1, 3])

# Select rows from position 5 to 10
print(df.iloc[5:11])

# Check which employees have a salary greater than 7000
print(df["Salary"] > 7000)

# Select employees with salary greater than 10000
print(df[df["Salary"] > 10000])


# ============================================
# Pandas Indexing and Filtering
# ============================================

# Create a DataFrame
df = pd.DataFrame(
    {
        "A": [1, 2, 3],
        "B": [4, 5, 6]
    },
    index=["X", "Y", "Z"]
)

print("DataFrame:")
print(df)

print("#" * 50)

# ============================================
# iat - Access a single value by position
# ============================================

print("Using iat:")
print(df.iat[1, 0])

print("#" * 50)

# ============================================
# at - Access a single value by label
# ============================================

print("Using at:")
print(df.at["Y", "A"])

print("#" * 50)

# ============================================
# iloc - Access data by numerical position
# ============================================

print("Using iloc:")
print(df.iloc[1, 0])

print("#" * 50)

# ============================================
# loc - Access data by label
# ============================================

print("Using loc:")
print(df.loc["Y", "A"])