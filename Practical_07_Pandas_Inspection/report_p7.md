

# Practical 7: Python DataFrame Setup and Schema Validation

## Objective

The objective of this practical is to load a raw dataset using Pandas, explore its structure, and perform schema validation by analyzing columns, data types, missing values, and uniqueness.


## Tools Used

* Python
* Pandas Library
* Jupyter Notebook


## Dataset Description

The dataset was loaded from a CSV file containing raw business data. It includes multiple columns such as categorical and numerical fields used for analysis.


## Steps Performed

### 1. Data Loading

The dataset was successfully loaded into a Pandas DataFrame using `read_csv()`.

### 2. Data Exploration

Basic structure of the dataset was analyzed using:

* Shape of dataset (rows and columns)
* First few rows using `head()`
* Last few rows using `tail()`
* Column names
* Data types of each column

### 3. Schema Validation

A schema audit table was created with the following details:

* Column Name
* Data Type (dtype)
* Missing Values Count
* Unique Values Count
* Sample Value from each column

This helps in understanding data quality and structure.

### 4. Exporting Results

The schema audit table was exported as a CSV file:

04_python/outputs/tables/schema_audit.csv


## Key Observations

* Some columns contain missing values which may require cleaning.
* Data types are mixed (numeric, object, etc.), and may need conversion for analysis.
* Unique counts help identify categorical vs continuous variables.
* Sample values give a quick understanding of column content.

---

## Conclusion

The dataset was successfully loaded and analyzed. Schema validation provided a clear understanding of data structure and quality. This step is important before performing further data cleaning and analysis.

---

## Output Files

* Notebook: `07_dataframe_schema.ipynb`
* Schema Audit File: `schema_audit.csv`
