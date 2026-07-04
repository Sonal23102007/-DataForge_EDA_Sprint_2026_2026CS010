# Practical 5 Report\n\nAdd your DAX modeling details here.\n
# Practical 5: Power BI Model, Measures and KPI Logic

## Objective

The objective of this practical was to understand Power BI data modeling, create measures using DAX, and design KPI logic for business insights.

---

## Tasks Performed

1. Created the Power BI file:
   **p5_powerbi_model_dax.pbix**

2. Loaded the cleaned dataset into Power BI and verified relationships in Model View.

3. Created DAX Measures:

   * **Total Sales** = SUM('Dataset'[Sales])
   * **Total Profit** = SUM('Dataset'[Profit])
   * **Order Count** = DISTINCTCOUNT('Dataset'[Order ID])
   * **Profit Margin** = DIVIDE([Total Profit], [Total Sales])
   * **Average Discount** = AVERAGE('Dataset'[Discount]) *(if available)*

4. Created a calculated column (only if needed):

   * Example: **Order Size Category** based on Sales value (Small / Medium / Large)

5. Created a Date Table / Date Hierarchy:

   * Extracted Year, Month for time-based analysis
   * Connected Date table with Order Date column

6. Verified Model View:

   * Checked relationships between tables
   * Ensured star schema structure (if applicable)

7. Captured screenshots:

   * Model View
   * Measures list

---

## Observations

* Measures allow dynamic aggregation based on filters and visuals.
* Data modeling improves performance and clarity of analysis.
* KPI logic helps in summarizing business performance quickly.

---

## Report Questions

### 1. What is the difference between a column and a measure?

A **column** is calculated row-by-row and stored in the dataset, increasing file size. It is static and does not change based on filters.

A **measure**, on the other hand, is calculated dynamically based on the current filter context in reports. Measures are not stored physically and are more efficient for aggregations like sum, average, and counts.

---

### 2. Which KPI would you put on top of the dashboard and why?

The most important KPI to place at the top of the dashboard would be **Total Sales**, because it gives a quick overview of overall business performance. It is the primary indicator of revenue generation and helps stakeholders immediately understand how the business is performing.

Additionally, **Profit Margin** can also be important as it shows how efficiently the business is converting sales into profit.

---

## Conclusion

This practical helped in understanding how Power BI handles data modeling and DAX measures. It highlighted the importance of KPIs in dashboards and how measures provide flexible and dynamic insights.
