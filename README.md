# Data-Cleaning-and-Visualization-Project
Data Cleaning and Visualization project using Python, Pandas, Matplotlib, and Seaborn. The project performs data preprocessing, handles missing values, removes duplicates, detects outliers, generates visualizations, and creates a cleaned dataset with an automated analysis report.
# Data Cleaning and Visualization Project

## Project Overview

This project demonstrates the process of cleaning, preprocessing, and visualizing data using Python. The objective is to improve data quality by handling missing values, removing duplicates, detecting outliers, and generating meaningful visualizations for data analysis.

---

## Objectives

- Load and analyze raw data.
- Handle missing values.
- Remove duplicate records.
- Detect potential outliers.
- Generate visualizations for better insights.
- Save the cleaned dataset.
- Create an automated data cleaning report.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## Project Structure

Data-Cleaning-and-Visualization-Project/

├── data/
│   └── raw_dataset.csv
│
├── cleaned_data/
│   └── cleaned_dataset.csv
│
├── images/
│   ├── missing_values.png
│   ├── correlation_heatmap.png
│   ├── hist_*.png
│   ├── box_*.png
│   └── bar_*.png
│
├── reports/
│   └── Data_Cleaning_Report.txt
│
├── data_cleaning.py
├── requirements.txt
├── README.md
└── .gitignore

---

## Dataset

The dataset contains employee-related information such as:

- Employee ID
- Age
- Gender
- Department
- Experience
- Salary
- Performance Score

The dataset intentionally includes:

- Missing values
- Duplicate records

These issues are cleaned during the preprocessing stage.

---

## Data Cleaning Tasks

The project performs the following operations:

### Missing Value Handling

- Numerical columns are filled using median values.
- Categorical columns are filled using mode values.

### Duplicate Removal

- Duplicate records are detected and removed.

### Outlier Detection

- Outliers are identified using the Interquartile Range (IQR) method.

---

## Visualizations Generated

### Missing Values Heatmap

Displays missing data distribution.

### Histograms

Shows data distribution for numerical columns.

### Boxplots

Helps identify outliers and data spread.

### Bar Charts

Displays frequency distributions for categorical variables.

### Correlation Heatmap

Shows relationships between numerical features.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/Data-Cleaning-and-Visualization-Project.git
