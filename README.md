# BMW Model Sales Performance Analysis

## Project Overview

This project analyzes worldwide BMW vehicle sales data to identify patterns in **sales performance, pricing, fuel type, transmission, vehicle models, and regional demand**.

The analysis combines **data cleaning, exploratory data analysis, visualization, correlation analysis, statistical hypothesis testing, and time-series analysis** to transform raw automotive sales data into actionable business insights.

The goal of the project is to understand the factors associated with BMW sales and pricing and use those findings to support decisions related to **regional strategy, product positioning, pricing, and inventory planning**.

---

## Business Problem

Automotive manufacturers operate across different regions, vehicle segments, fuel technologies, and pricing levels. Understanding how these factors relate to sales performance can help organizations make better strategic decisions.

This project focuses on answering questions such as:

* Which BMW models demonstrate stronger sales performance?
* How does vehicle pricing vary across geographic regions?
* Are average BMW prices significantly different across fuel types?
* Are average prices significantly different across regions?
* Is there an association between fuel type and transmission type?
* What relationships exist among engine size, mileage, price, and sales volume?
* How has BMW sales volume changed over time?
* What insights can be used to improve regional marketing and inventory decisions?

---

## Dataset

The project uses the **BMW Worldwide Sales Records (2010–2024)** dataset available through Kaggle.

**Source:** Kaggle — BMW Worldwide Sales Records 2010–2024

The dataset contains information related to BMW vehicle characteristics and sales performance, including variables such as:

* Model
* Year
* Region
* Fuel Type
* Transmission
* Engine Size
* Mileage
* Vehicle Price
* Sales Volume

---

## Tools & Technologies

* **Python**
* **Pandas**
* **NumPy**
* **Matplotlib**
* **Seaborn**
* **SciPy**
* **Jupyter Notebook**
* **Statistical Hypothesis Testing**
* **Exploratory Data Analysis**

---

## Project Workflow

### 1. Data Cleaning

The dataset was prepared for analysis through several preprocessing steps.

The process included:

* Identifying missing values
* Replacing missing numeric values using column means
* Removing remaining incomplete observations
* Checking for duplicate records
* Identifying potential outliers
* Removing extreme observations using the **Interquartile Range (IQR)** method

Outlier treatment was applied particularly to:

* `Price_USD`
* `Sales_Volume`

This helped reduce the influence of extreme observations on the subsequent analysis.

---

## 2. Exploratory Data Analysis

Descriptive statistics and visual analysis were used to understand the structure and distribution of the data.

The analysis examined:

* Sales performance across BMW models
* Fuel type and transmission distribution
* Regional sales activity
* Regional pricing differences
* Relationships between numerical variables
* Changes in sales volume over time

---

## 3. Sales Volume by BMW Model

Boxplots were used to compare the distribution of sales volume across BMW models.

This visualization helps identify:

* Differences in median sales
* Variation in sales performance
* Models with more consistent demand
* Models with unusually high or low sales observations

Unlike a simple average, the boxplot provides insight into both the center and spread of sales performance.

---

## 4. Fuel Type vs. Transmission

The distribution of transmission types was compared across different fuel categories.

This analysis helps identify whether certain fuel technologies are more commonly associated with particular transmission configurations.

Understanding these combinations may support:

* Product portfolio planning
* Manufacturing decisions
* Customer segmentation
* Marketing strategy

---

## 5. Regional Sales Analysis

Sales records were analyzed across geographic regions to identify differences in market activity.

The analysis helps highlight regions with stronger representation in the dataset and provides a foundation for comparing BMW sales performance across markets.

Regional differences may indicate opportunities for:

* Market-specific promotions
* Inventory allocation
* Regional product positioning
* Expansion strategies

---

## 6. Regional Pricing Analysis

Vehicle prices were compared across regions using boxplots.

This analysis evaluates differences in:

* Median price
* Price variability
* Regional pricing ranges
* Potential premium markets

The results can help determine whether different geographic markets support different pricing strategies.

---

## 7. Correlation Analysis

A correlation matrix was created for key continuous variables:

* Engine Size
* Mileage
* Vehicle Price
* Sales Volume

A heatmap was used to visualize the strength and direction of relationships between these variables.

Correlation analysis helps identify which numerical features may move together and provides direction for additional statistical or predictive analysis.

---

## Statistical Analysis

Statistical hypothesis testing was used to determine whether several observed differences in the dataset were statistically meaningful.

A **95% confidence level** was used throughout the analysis.

---

### Hypothesis Test 1: Fuel Type vs. Average Vehicle Price

A one-way **ANOVA** was used to compare average vehicle prices across fuel types.

**Null Hypothesis (H₀):**

There is no significant difference in average BMW vehicle price between fuel types.

**Alternative Hypothesis (H₁):**

At least one fuel type has a significantly different average vehicle price.

This test helps determine whether fuel technology may be associated with different pricing levels.

---

### Hypothesis Test 2: Region vs. Average Vehicle Price

A second one-way **ANOVA** was used to determine whether BMW prices differ significantly across geographic regions.

**Null Hypothesis (H₀):**

Average BMW vehicle prices are the same across all regions.

**Alternative Hypothesis (H₁):**

At least one region has a significantly different average vehicle price.

The analysis found evidence of statistically significant differences in average pricing across regions.

This suggests that regional market characteristics may play an important role in BMW pricing.

---

### Hypothesis Test 3: Fuel Type vs. Transmission

A **Chi-Square Test of Independence** was used to evaluate the relationship between fuel type and transmission.

**Null Hypothesis (H₀):**

Fuel type and transmission type are independent.

**Alternative Hypothesis (H₁):**

Fuel type and transmission type are associated.

The analysis identified an association between these categorical variables, suggesting that transmission configurations are not distributed equally across fuel technologies.

---

## Time-Series Analysis

BMW sales volume was analyzed over time using a line chart.

The analysis was designed to identify:

* Long-term sales trends
* Periods of growth or decline
* Cyclical patterns
* Changes in product demand over time

Understanding these patterns can help organizations improve forecasting and inventory planning.

---

## Key Findings

The analysis produced several important findings:

* BMW vehicle prices vary across both **fuel types and geographic regions**.
* Statistical testing indicates significant differences in average vehicle prices between certain groups.
* Fuel type and transmission configuration show evidence of an association.
* Sales performance varies considerably across BMW models.
* Certain regions demonstrate stronger sales activity than others.
* Vehicle pricing differs across regional markets.
* Sales volume shows noticeable changes and patterns over time.
* Model, market, pricing, and vehicle characteristics all provide useful dimensions for understanding BMW sales performance.

---

## Business Recommendations

### 1. Develop Regional Pricing Strategies

Because vehicle pricing differs across regions, BMW could consider market-specific pricing approaches rather than applying identical strategies globally.

Regions that consistently support higher average prices may provide opportunities for:

* Premium configurations
* Higher-value packages
* Upselling opportunities

---

### 2. Prioritize High-Performing Models

Models demonstrating consistently strong sales should receive greater attention in:

* Marketing campaigns
* Dealer inventory
* Production planning
* Promotional strategy

Lower-performing models should be evaluated to determine whether performance is related to pricing, region, product positioning, or customer preference.

---

### 3. Align Inventory With Regional Demand

Regional differences in sales activity suggest that vehicle allocation should reflect local demand patterns.

BMW could use historical regional sales data to better determine:

* Which models to stock
* Which fuel types to prioritize
* Appropriate inventory levels
* Market-specific product mixes

---

### 4. Monitor Fuel-Type Preferences

As vehicle markets evolve, BMW should continue monitoring demand across:

* Petrol
* Diesel
* Electric
* Other fuel technologies

Understanding changing preferences can improve product development and market positioning.

---

### 5. Incorporate Sales Trends Into Forecasting

Historical time-series patterns can be incorporated into future forecasting models.

This could support:

* Production planning
* Dealer inventory management
* Promotional timing
* Demand forecasting
* Regional resource allocation

---

## Skills Demonstrated

This project demonstrates practical experience in:

* Data Cleaning
* Exploratory Data Analysis
* Data Visualization
* Outlier Detection
* Statistical Analysis
* ANOVA
* Chi-Square Testing
* Correlation Analysis
* Time-Series Analysis
* Business Analytics
* Translating Analytical Results into Business Recommendations

---

## Potential Future Enhancements

The project could be expanded by incorporating:

### Predictive Modeling

Build machine learning models to predict:

* Vehicle price
* Sales volume
* Regional demand

Potential algorithms could include:

* Linear Regression
* Random Forest
* XGBoost

### Customer and Market Segmentation

Clustering techniques could identify groups of vehicles or markets with similar characteristics.

### Interactive Dashboard

The analysis could be transformed into an interactive **Power BI or Tableau dashboard** for exploring:

* Model performance
* Regional sales
* Fuel-type trends
* Pricing patterns
* Historical performance

### Forecasting

Time-series forecasting models could be developed to estimate future BMW sales demand.

---

## Conclusion

This project demonstrates how exploratory analytics and statistical testing can be applied to automotive sales data to uncover meaningful business patterns.

By analyzing BMW sales across **models, regions, fuel technologies, transmission types, pricing levels, and time**, the project provides insights that could support better decisions in pricing, marketing, product strategy, and inventory management.

The project also demonstrates the ability to move beyond visualization by using formal statistical testing to determine whether observed differences in the data are statistically significant.

---

## Author

**Siddharth Shenoy**
MS Business Analytics & Information Management
Purdue University

**Skills:** Python | SQL | Power BI | Machine Learning | Statistical Analysis | Business Analytics
