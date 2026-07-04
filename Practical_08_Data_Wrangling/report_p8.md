
# Practical 8: Python Cleaning, Type Conversion and Feature Engineering

## Objective

The objective of this practical is to clean the raw dataset, handle missing values, convert data types, and create new features to make the dataset ready for analysis.


## Tools Used

* Python
* Pandas Library
* Jupyter Notebook

## Dataset Description

The dataset contains raw business data with a mix of categorical, numerical, and date columns. The data required cleaning and transformation before further analysis.

## Steps Performed

### 1. Handling Duplicates

Duplicate rows were checked using `df.duplicated()`.

* Duplicates were removed where found to avoid incorrect analysis.
* If no duplicates were present, it was documented.

### 2. Handling Missing Values

* **Categorical Columns:**
  Missing values were replaced with `"Unknown"` to maintain consistency.

* **Numerical Columns:**
  Missing values were handled using mean/median imputation (depending on data distribution) or flagged for analysis.

### 3. Data Type Conversion

* Date columns were converted to datetime format using `pd.to_datetime()`.
* Correct data types were ensured for numerical and categorical columns.

### 4. Feature Engineering

At least two new columns were created:

* **Month / Year Column:**
  Extracted from the date column to enable time-based analysis.

* **Profit Margin (or similar metric):**
  Created using existing columns (e.g., Profit / Sales) to evaluate business performance more effectively.

### 5. Reusable Script

A reusable Python script `clean_dataset.py` was created to automate the cleaning process for future datasets.

### 6. Exporting Cleaned Data

The cleaned dataset was saved as:

```id="5hvq92"
01_data/processed/dataforge_cleaned.csv
```


## Key Observations

* Missing values were present in both categorical and numerical columns.
* Data type inconsistencies were corrected.
* Feature engineering improved the analytical value of the dataset.


## Report Questions

### 1. What cleaning decision could affect business conclusions?

The method used to handle missing numerical values (such as mean or median imputation) can significantly affect business conclusions. For example, replacing missing sales values with the mean may distort actual performance trends, especially if the data is skewed.

### 2. Which engineered feature is most useful and why?

The **Profit Margin** feature is the most useful because it provides a clear measure of profitability relative to sales. It helps in comparing performance across categories, regions, or time periods more effectively than absolute profit values.



## Conclusion

The dataset was successfully cleaned and transformed. Missing values, duplicates, and data types were handled appropriately. Feature engineering enhanced the dataset, making it suitable for deeper analysis and business insight

## Output Files

* Notebook: `08_cleaning_features.ipynb`
* Script: `clean_dataset.py`
* Cleaned Dataset: `dataforge_cleaned.csv`
