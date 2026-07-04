
# Practical 9: Python EDA Tables, Grouping and Statistical Insights

## Objective

The objective of this practical is to perform Exploratory Data Analysis (EDA) using Pandas by generating summary statistics, grouped tables, ranking insights, and exporting useful tables for analysis.


## Tools Used

* Python
* Pandas Library
* Jupyter Notebook


## Dataset Description

The cleaned dataset (`dataforge_cleaned.csv`) was used for analysis. It contains structured business data with numerical and categorical columns suitable for statistical and grouped analysis.


## Steps Performed

### 1. Summary Statistics

* Generated descriptive statistics for all numeric columns using `describe()`.
* Exported the summary table for further analysis.

### 2. Missing Value Analysis

* Created a missing-value percentage table for all columns.
* This helped identify data quality issues and completeness.

### 3. Grouped Tables (Using groupby)

At least four grouped tables were created to analyze patterns:

* Sales/Revenue by Category
* Profit by Region
* Order Count by Segment
* Monthly Sales Trend (using date features)

These tables helped in understanding performance across different dimensions.

### 4. Ranking Tables

* Created **Top 10** and **Bottom 10** tables based on a meaningful metric (e.g., Sales or Profit).
* These tables highlight best and worst performing categories, products, or regions.

### 5. Exporting Tables

All generated tables were exported as CSV files for reporting and further use.



## Key Insights

1. A few categories contribute the majority of total sales, indicating uneven distribution.
2. Some regions show high sales but relatively low profit, suggesting higher costs or discounts.
3. The bottom 10 performers consistently show low profitability and may require attention.
4. Monthly trends indicate fluctuations, showing possible seasonal patterns in sales.
5. Missing values are minimal in key columns, ensuring reliability of analysis.



## Conclusion

EDA was successfully performed using statistical summaries, grouped analysis, and ranking techniques. The generated tables provide valuable insights into business performance and help in identifying trends, strengths, and areas of improvement.


## Output Files

* Notebook: `09_python_eda_tables.ipynb`
* Summary Table: `describe_summary.csv`
* Missing Value Table: `missing_percentage.csv`
* Grouped Tables: multiple CSV files
* Ranking Tables: `top10.csv`, `bottom10.csv`
