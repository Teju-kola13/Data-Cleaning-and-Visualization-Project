import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# =====================================
# CREATE OUTPUT FOLDERS
# =====================================
os.makedirs("cleaned_data", exist_ok=True)
os.makedirs("images", exist_ok=True)
os.makedirs("reports", exist_ok=True)

# =====================================
# LOAD DATASET
# =====================================
try:
    df = pd.read_csv("data/raw_dataset.csv")
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("ERROR: data/raw_dataset.csv not found.")
    exit()

# =====================================
# BASIC INFORMATION
# =====================================
print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values Before Cleaning:")
print(df.isnull().sum())

# =====================================
# HANDLE MISSING VALUES
# =====================================
for col in df.select_dtypes(include=np.number).columns:
    df[col] = df[col].fillna(df[col].median())

for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# =====================================
# REMOVE DUPLICATES
# =====================================
duplicates_before = df.duplicated().sum()

df = df.drop_duplicates()

duplicates_after = df.duplicated().sum()

print("\nDuplicates Removed:", duplicates_before)

# =====================================
# SAVE CLEANED DATASET
# =====================================
df.to_csv(
    "cleaned_data/cleaned_dataset.csv",
    index=False
)

# =====================================
# MISSING VALUES VISUALIZATION
# =====================================
plt.figure(figsize=(10, 5))

sns.heatmap(
    df.isnull(),
    cbar=False
)

plt.title("Missing Values Heatmap")

plt.tight_layout()

plt.savefig(
    "images/missing_values.png"
)

plt.close()

# =====================================
# NUMERICAL COLUMNS
# =====================================
num_cols = df.select_dtypes(include=np.number).columns

# =====================================
# HISTOGRAMS
# =====================================
for col in num_cols:

    plt.figure(figsize=(8, 5))

    plt.hist(
        df[col],
        bins=10
    )

    plt.title(
        f"Histogram - {col}"
    )

    plt.tight_layout()

    plt.savefig(
        f"images/hist_{col}.png"
    )

    plt.close()

# =====================================
# BOXPLOTS
# =====================================
for col in num_cols:

    plt.figure(figsize=(8, 5))

    plt.boxplot(df[col])

    plt.title(
        f"Boxplot - {col}"
    )

    plt.tight_layout()

    plt.savefig(
        f"images/box_{col}.png"
    )

    plt.close()

# =====================================
# BAR CHARTS
# =====================================
cat_cols = df.select_dtypes(
    include="object"
).columns

for col in cat_cols:

    plt.figure(figsize=(8, 5))

    df[col].value_counts().plot(
        kind="bar"
    )

    plt.title(
        f"Bar Chart - {col}"
    )

    plt.tight_layout()

    plt.savefig(
        f"images/bar_{col}.png"
    )

    plt.close()

# =====================================
# CORRELATION HEATMAP
# =====================================
if len(num_cols) > 1:

    corr = df[num_cols].corr()

    plt.figure(figsize=(10, 6))

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm"
    )

    plt.title(
        "Correlation Heatmap"
    )

    plt.tight_layout()

    plt.savefig(
        "images/correlation_heatmap.png"
    )

    plt.close()

# =====================================
# OUTLIER ANALYSIS
# =====================================
outlier_report = []

for col in num_cols:

    q1 = df[col].quantile(0.25)
    q3 = df[col].quantile(0.75)

    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    outliers = df[
        (df[col] < lower) |
        (df[col] > upper)
    ]

    outlier_report.append(
        f"{col}: {len(outliers)} outliers"
    )

# =====================================
# GENERATE REPORT
# =====================================
with open(
    "reports/Data_Cleaning_Report.txt",
    "w",
    encoding="utf-8"
) as report:

    report.write(
        "DATA CLEANING AND VISUALIZATION REPORT\n"
    )

    report.write(
        "=" * 60 + "\n\n"
    )

    report.write(
        f"Rows: {df.shape[0]}\n"
    )

    report.write(
        f"Columns: {df.shape[1]}\n\n"
    )

    report.write(
        f"Duplicates Removed: {duplicates_before}\n\n"
    )

    report.write(
        "Missing Values After Cleaning\n"
    )

    report.write(
        str(df.isnull().sum())
    )

    report.write(
        "\n\n"
    )

    report.write(
        "Statistical Summary\n"
    )

    report.write(
        str(df.describe())
    )

    report.write(
        "\n\nOutlier Analysis\n"
    )

    for item in outlier_report:
        report.write(
            item + "\n"
        )

print("\n" + "=" * 60)
print("DATA CLEANING COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nGenerated Files:")
print("cleaned_data/cleaned_dataset.csv")
print("images/missing_values.png")
print("images/correlation_heatmap.png")
print("reports/Data_Cleaning_Report.txt")