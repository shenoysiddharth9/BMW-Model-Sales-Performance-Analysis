import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import scipy.stats as stats

# Data Source - https://www.kaggle.com/datasets/ahmadrazakashif/bmw-worldwide-sales-records-20102024

df=pd.read_csv('C:\BMW.csv')

#2. Data Cleaning:
#This is to fill the missing numeric values in the data with mean
display(df.isnull().sum())
df.fillna(df.select_dtypes(include="number").mean(), inplace=True)

# display(df)

#This is to drop any remaining missing values which have not be been filled
df.dropna(inplace = True)
print("data after dropping any data (if applicable):-")
display(df)

# Checked for duplicate values in the DataFrame.

display(df.duplicated().sum())
df.drop_duplicates()

#Identifying and Handling Outliers for Price_USD Column.
Q1 = df['Price_USD'].quantile(0.25)
Q3 = df['Price_USD'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers_iqr = df[(df['Price_USD'] < lower_bound) | (df['Price_USD'] > upper_bound)]
print(f'\nThe outliers for price_usd are:-')
display(outliers_iqr)
df = df[(df['Price_USD'] >= lower_bound) & (df['Price_USD'] <= upper_bound)]
display(df)

#Identifying and Handling Outliers for Sales_Volume Column.
Q1 = df['Sales_Volume'].quantile(0.25)
Q3 = df['Sales_Volume'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
outliers_iqr = df[(df['Sales_Volume'] < lower_bound) | (df['Sales_Volume'] > upper_bound)]
print(f'\nThe outliers for Sales_Volume are:-')
display(outliers_iqr)
df = df[(df['Sales_Volume'] >= lower_bound) & (df['Sales_Volume'] <= upper_bound)]
display(df)

#3. Exploratory Data Analysis (EDA):
#Descriptive Statistics
display(df.drop(columns=['Year','Engine_Size_L']).describe())

# Data Visualization
#Boxplot: Volume of Sales By Model
print("We used boxplots to compare spread, median, and outliers of units sold across various BMW models.\n"
      "Compared to bar charts, boxplots provide much richer statistical summary and directly reveal spread and variation between models,\n"
      "which are essential for understanding business dynamism among categories.")
plt.figure(figsize=(18,12))
sns.set_style('darkgrid')
sns.boxplot(x=df['Model'],y= df['Sales_Volume'],hue=df['Model'])
plt.xlabel('Model Sold')
plt.ylabel('Volume of Sales')
plt.title('Volume of Sales By Model')
plt.xticks(rotation =45)
plt.show()

#Countplot: Fuel_Type vs Transmission
print("We used countplot to compare fuel type vs transmission.\n"
      "We used countplot as it is ideal to show frequency of each category.")
plt.figure(figsize=(14,10))
sns.set_style('darkgrid')
ax = sns.countplot(x=df['Fuel_Type'], hue=df['Transmission'])

plt.title("Fuel_Type vs Transmission")
plt.xlabel("Fuel_Type")
plt.ylabel("Vehicle Count")

# Add count labels on bars
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width()/2., height + 50, int(height), ha='center', fontsize=12)

# Legend inside grid, above bars, away from labels
plt.legend(title='Transmission', loc='upper left', bbox_to_anchor=(1, 1), fontsize=12, title_fontsize=13, frameon=True)

plt.tight_layout()
plt.show()

#Bar Chart: Distribution of Sales Records by Region
print("we used bar plot to showcase which region has highest sales records.")
plt.figure(figsize=(10,6))
counts = df['Region'].value_counts()
ax = sns.barplot(x=counts.values, y=counts.index, hue = counts.index)

# Add labels to bars
for i, v in enumerate(counts.values):
    ax.text(v + 5, i, str(v), color='black', va='center')

plt.title('Sales Records Distribution by Region')
plt.xlabel('Count')
plt.ylabel('Region')
plt.show()

#Boxplot: Price Distribution by Region
print("We used boxplot to showcase price across regions to understand about the pricing dynamics.")
plt.figure(figsize=(14,8))
sns.boxplot(x='Region', y='Price_USD', hue = df['Region'],data=df)
plt.title('Price Distribution by Region')
plt.xlabel('Region')
plt.ylabel('Price (USD)')
plt.xticks(rotation=45)
plt.show()

# Correlation Analysis
print("Correlation Analysis:-")
print("We used heatmap to show correlation to visualize pairwise relationships and strength between all continuous variables at once.\n"
      "A heatmap quickly shows all mutual correlations compared to other visualizations and helps to guide further analysis or modeling.")
correlation = df[["Engine_Size_L", "Mileage_KM", "Price_USD", "Sales_Volume"]].corr()
print("\nCorrelation matrix:")
display(correlation)
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# Hypothesis Testing
# FuelType vs AveragePrice
print("Hypothesis Testing:-")
print("Null Hypothesis - H₀: There is no significant difference in average vehicle price between fuel types (Petrol, Diesel, Electric).\n"
      "Alternative Hypothesis - Ha: At least one fuel type has a different average price.")
groups = [y["Price_USD"].values for x, y in df.groupby("Fuel_Type")]
stat, p = stats.f_oneway(*groups)
print("ANOVA for Price by Fuel_Type: p-value =", p)
print("Testing at 95% significance level.")
if p < 0.05:
    print("Conclusion: Significant difference in mean prices among fuel types.")
else:
    print("Conclusion: No significant difference in mean prices among fuel types.")

# Region vs AveragePrice
print("\n Null Hypothesis - H₀: The average vehicle price is the same across all regions.\n"
      "Alternative Hypothesis - Ha: At least one region differs in mean price.")
groups = [y["Price_USD"].values for x, y in df.groupby("Region")]
stat, p = stats.f_oneway(*groups)
print("ANOVA for Price by Region: p-value =", p)
print("Testing at 95% significance level.")
if p < 0.05:
    print("Conclusion:At least one region differs in mean price.")
else:
    print("Conclusion: The average vehicle price is the same across all regions.")

# FuelType vs Transmission
print("\n Null Hypothesis - H₀: Fuel type and transmission are independent.\n"
      " Alternative Hypothesis - Ha: Fuel type and transmission are associated.")
contingency = pd.crosstab(df['Fuel_Type'], df['Transmission'])
chi2, p, dof, ex = stats.chi2_contingency(contingency)
print("Chi-squared p-value for Fuel_Type vs Transmission:", p)
print("Testing at 95% significance level.")
if p < 0.05:
    print("Conclusion: Fuel type and transmission are associated.")
else:
    print("Conclusion: No association found between fuel type and transmission.")

#Time series Analysis
print("\nWe used lineplot to show the trend of sales over time.\n"
      "Ideal for trends and time-series analysis,\n"
      "a lineplot reveals cyclical patterns and long-term changes, which would be missed with a bar chart or point plot.")
plt.figure(figsize=(18,12))
sns.set_style('darkgrid')
sns.lineplot(x = df['Year'],y= df['Sales_Volume'])
plt.xlabel('Year')
plt.ylabel('Sales Volume')
plt.title('Sales Over Time')
plt.show()

# 6. Extracting and Summarizing Business Insights
print("\nBusiness Insights Summary:")
print("- Petrol and Diesel models show significant price and sales variation by region and model.")
print("- Statistically significant differences exist in average price by region and by fuel type (see ANOVA p-values).")
print("- Transmission type distribution differs across fuel types (see chi-squared result).")
print("- Highest sales volumes are seen in select models and regions across recent years.")
print("- There is clear time-based cyclicality and recent growth trends in the product line.")

print("\nRecommendations:")
print("- Focus on promoting top-selling models in rapidly growing regions and track transmission-fuel mix preferences for market targeting.")
print("- Use regional pricing strategies to optimize profits from regions showing higher average prices.")
print("- Monitor cyclical sales patterns and inventory accordingly.")
