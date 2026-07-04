
# Practical 4: Power BI Power Query Cleaning Pipeline

## Objective

The objective of this practical was to use Power BI Power Query to clean and transform raw data, and to build a reusable ETL (Extract, Transform, Load) pipeline.


## Tasks Performed

1. Imported the file **dataset_raw.csv** into Power BI Desktop.

2. Opened Power Query Editor and performed initial cleaning steps:

   * Promoted first row as headers
   * Checked and corrected data types (Text, Number, Date)
   * Removed obvious errors and null values where necessary

3. Created a conditional column:

   * **Profit Status**

     * Profit > 0 → "Profit"
     * Profit ≤ 0 → "Loss"

4. Created extracted date columns:

   * **Year** from Order Date
   * **Month** from Order Date

5. Verified all applied steps in the Applied Steps pane to ensure proper transformation flow.

6. Copied the Power Query **Advanced Editor (M Code)** and saved it in:

   * 03_powerbi/p4_power_query_m_code.txt

7. Saved the Power BI file as:

   * **03_powerbi/p4_power_query_pipeline.pbix**


## Observations

* Power Query provides a structured and step-by-step approach to data cleaning.
* Each transformation is recorded, making the process transparent and reusable.
* Data types and errors can be handled more efficiently compared to manual methods.

---

## Report Questions

### 1. How is Power Query different from manual Excel cleaning?

Power Query is different from manual Excel cleaning because it automates the data cleaning process. In Excel, cleaning is usually done manually using formulas and filters, which is time-consuming and not easily repeatable. In contrast, Power Query records each transformation step, allowing the same process to be applied automatically to new data. This makes it more efficient, consistent, and scalable.

---

### 2. Which transformation would save time when new CSV data arrives?

The most time-saving transformation is the **automated sequence of applied steps in Power Query**, especially tasks like promoting headers, setting data types, and creating conditional and date columns. Once these steps are defined, Power BI can simply refresh the data when a new CSV file is added, and all transformations are applied automatically without repeating the work.

---

## Conclusion

This practical demonstrated how Power Query can be used to build a reusable data cleaning pipeline. It is more powerful than manual Excel cleaning and is especially useful when working with frequently updated datasets.
