#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Title= 
'''
IN-DEPTH ANALYSIS OF ADIDAS SALES OPERATING PROFIT (2020-2021)

'''

# Introduction = 
'''
In this analysis,I  aim to evaluate the operating profit trends of Adidas across different regions 
for the years 2020 and 2021. By examining the percentage change in operating profit, I set out to
uncover which regions thrived and which faced challenges during this time. 

Understanding these trends is not just a numbers game; it's essential for making informed business
decisions. This insight will allow Adidas as a manufacturing company to allocate resources more
effectively, optimize product offerings, and tailor marketing strategies to meet the unique needs
of each region. Ultimately, this analysis serves as a foundation for driving growth and improving 
overall financial performance, helping the company as whole navigate the ever-changing landscape of 
the retail market.

'''


# In[2]:


#importing the neccessary libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


# loading the dataset in to notebook

adidas_sales_data = pd.read_csv("C:\\Users\\HP\\OneDrive\\Documents\\ADIDDASSALESSQLCLEANEDDATA.csv")


# In[4]:


# the first 5 rows of the dataset

adidas_sales_data.head()


# In[5]:


# Checkinf for missing values 

adidas_sales_data.info()


# In[6]:


# checking the list of columns in adidas_sales_data 

print(adidas_sales_data.columns)


# In[39]:


# trying to Replace spaces in all column names with underscores
adidas_sales_data.columns = adidas_sales_data.columns.str.replace(' ', '_')

# Ensuring the correct format for 'Invoice_Date' column name if needed
adidas_sales_data.rename(columns={'Invoice_Date': 'Invoice_date'}, inplace=True)
print(adidas_sales_data.columns)


# In[40]:


# Extracting the year from 'Invoice_date'
adidas_sales_data['Year'] = pd.to_datetime(adidas_sales_data['Invoice_date']).dt.year

# Calculation total operating profit for each year
total_profit = adidas_sales_data.groupby('Year')['Operating_Profit'].sum().reset_index()

# results
print(total_profit)



# In[20]:


# Analysis of the results in percentages
profit_2020 = total_profit[total_profit['Year'] == 2020]['Operating_Profit'].values[0]  
profit_2021 = total_profit[total_profit['Year'] == 2021]['Operating_Profit'].values[0]  
percentage_change = ((profit_2021 - profit_2020) / profit_2020) * 100

print(f'Total Operating Profit for 2020: ${profit_2020:.2f}')  # Formatting for currency
print(f'Total Operating Profit for 2021: ${profit_2021:.2f}')  # Formatting for currency
print(f'Percentage Change from 2020 to 2021: {percentage_change:.2f}%')


# In[8]:


# Bar plot for total operating profit

# creating fig. size
plt.figure(figsize=(10, 6))

sns.barplot(x='Year', y='Operating_Profit', data=total_profit)  
plt.title('Total Operating Profit for Adidas (2020-2021)')
plt.xlabel('Year')
plt.ylabel('Total Operating Profit')

plt.show()


# In[10]:


# Data preparation
years = ['2020', '2021']
profits = [profit_2020, profit_2021]

# Creating a fig. size
plt.figure(figsize=(10, 6))

# Bar plot for total operating profit by year
sns.barplot(x=years, y=profits, )  
plt.title('Total Operating Profit for Adidas (2020 vs 2021)')
plt.xlabel('Year')
plt.ylabel('Total Operating Profit ($)')
plt.ylim(0, max(profits) * 1.1)  

# percentage change
plt.text(0.5, max(profits) * 0.8, f'Percentage Change: {percentage_change:.2f}%', 
         ha='center', fontsize=14, color='black', weight='bold')

# Show the plot
plt.tight_layout()
plt.show()


# In[11]:


# total operating profit for each region group by Year
profit_by_region = adidas_sales_data.groupby(['Year', 'Region'])['Operating_Profit'].sum().reset_index()

# results
profit_by_region


# In[21]:


# calculation of percentage change
profit_pivot = profit_by_region.pivot(index='Region', columns='Year', values='Operating_Profit').reset_index() 
profit_pivot['Percentage Change'] = ((profit_pivot[2021] - profit_pivot[2020]) / profit_pivot[2020]) * 100

#'Percentage Change' to 2 decimal places
profit_pivot['Percentage Change'] = profit_pivot['Percentage Change'].round(2)

# result
profit_pivot


# In[12]:


# Plotting Operating Profit by Region for each year

# creating fig. size
plt.figure(figsize=(12, 8))

sns.barplot(x='Region', y='Operating_Profit', hue='Year', data=profit_by_region)  
plt.title('Total Operating Profit by Region for Adidas (2020 vs 2021)')
plt.xlabel('Region')
plt.ylabel('Total Operating Profit')
plt.legend(title='Year')

plt.show()


# In[23]:


# Ensure the pivoted data for percentage change is ready
profit_pivot = profit_by_region.pivot(index='Region', columns='Year', values='Operating_Profit').reset_index()
profit_pivot['Percentage Change'] = ((profit_pivot[2021] - profit_pivot[2020]) / profit_pivot[2020]) * 100
profit_pivot['Percentage Change'] = profit_pivot['Percentage Change'].round(2)

# style for the plots
sns.set(style="ticks")

# Create figure size
plt.figure(figsize=(14, 8))

# Bar plot for Percentage Change by Region
sns.barplot(x='Region', y='Percentage Change', data=profit_pivot, palette='viridis')

plt.title('Percentage Change in Operating Profit by Region (2021 vs 2020)')
plt.xlabel('Region')
plt.ylabel('Percentage Change (%)')

# Remove grid lines
plt.grid(False)


plt.tight_layout()
plt.show()


# In[15]:


# total operating profit for each product
profit_by_product = adidas_sales_data.groupby(['Year', 'Product'])['Operating_Profit'].sum().reset_index() 

# results
profit_by_product


# In[16]:


# Plotting Operating Profit by Product for each year

# creating fig. size
plt.figure(figsize=(14, 8))

sns.barplot(x='Product', y='Operating_Profit', hue='Year', data=profit_by_product)  # Changed 'Operating Profit' to 'Operating_Profit'
plt.title('Total Operating Profit by Product for Adidas (2020 vs 2021)')
plt.xlabel('Product')
plt.ylabel('Total Operating Profit')
plt.legend(title='Year')

plt.show()


# In[17]:


# Pivot data
'''
In this section of the analysis, I focus on calculating the percentage change in operating profit
for each product offered by Adidas between 2020 and 2021. By pivoting the data, I restructure it to 
have products as rows and the corresponding operating profits for each year as columns. This allows 
me to easily compare the performance of each product over the two years.

The percentage change is then calculated to understand how each product's profitability has evolved.
This information is crucial, as it helps identify which products are thriving and which may need 
attention or re-evaluation. Ultimately, this analysis informs strategic decisions, such as product 
development and marketing efforts, to enhance Adidas's overall performance in a competitive market.

'''






profit_product_pivot = profit_by_product.pivot(index='Product', columns='Year', values='Operating_Profit').reset_index() 

# Calculation of percentage change between 2021 and 2020
profit_product_pivot['Percentage Change'] = ((profit_product_pivot[2021] - profit_product_pivot[2020]) / profit_product_pivot[2020]) * 100

# Rounding the 'Percentage Change' to 2 decimal places
profit_product_pivot['Percentage Change'] = profit_product_pivot['Percentage Change'].round(2)

# Display the percentage change
profit_product_pivot


# In[18]:


# the style for the plots
sns.set(style="whitegrid")

# Creating a fig. size
plt.figure(figsize=(14, 8))

# Bar plot for Percentage Change by Product
sns.barplot(x='Product', y='Percentage Change', data=profit_product_pivot, palette='coolwarm')
plt.title('Percentage Change in Operating Profit by Product (2021 vs 2020)')
plt.xlabel('Product')
plt.ylabel('Percentage Change (%)')
plt.xticks() 

# Show the plot
plt.tight_layout()
plt.show()


# In[24]:


# total operating profit by Sales Method for each year
profit_by_sales_method = adidas_sales_data.groupby(['Year', 'Sales_Method'])['Operating_Profit'].sum().reset_index()

# results
profit_by_sales_method


# In[27]:


# total operating profit by Retailer for each year

profit_by_retailer = adidas_sales_data.groupby(['Year', 'Retailer'])['Operating_Profit'].sum().reset_index()
print(profit_by_retailer)


# In[28]:


# Showcasing the most profitable RETAILER for each year
most_profitable_retailer = profit_by_retailer.loc[profit_by_retailer.groupby('Year')['Operating_Profit'].idxmax()]

# result
most_profitable_retailer


# In[29]:


# total operating profit by Region and Sales Method for each year
profit_by_region_sales_method = adidas_sales_data.groupby(['Year', 'Region', 'Sales_Method'])['Operating_Profit'].sum().reset_index()

# profit distribution across regions and sales methods
profit_region_sales_pivot = profit_by_region_sales_method.pivot_table(index='Region', columns=['Year', 'Sales_Method'], values='Operating_Profit')

# result
profit_region_sales_pivot


# In[ ]:


'''
This table contains the total sales of Adidas product for the years 2020 and 2021 categorized by 
regions and mainly based on outlet, In-store, and Online sales. On an individual level, each cell
holds the operating profit and only in the operating profit do we find the year, region and sales
method.

Columns: These first three point values correspond to the years 2020 and 2021, while the last three
relate to the distinct sales approaches.
Rows: Each row represents one region: Midwest, Northeast, South, Southeast and West which enables the
user to filter sales region by year.


'''


# In[30]:


# total operating profit by Region and Retailer for each year
profit_by_region_retailer = adidas_sales_data.groupby(['Year', 'Region', 'Retailer'])['Operating_Profit'].sum().reset_index()

# profit distribution across regions and retailers
profit_region_retailer_pivot = profit_by_region_retailer.pivot_table(index='Region', columns=['Year', 'Retailer'], values='Operating_Profit')

# result
profit_region_retailer_pivot


# In[34]:


# creating fig. size
plt.figure(figsize=(12, 6))

sns.barplot(x='Sales_Method', y='Operating_Profit', hue='Year', data=profit_by_sales_method,)
plt.title('Operating Profit by Sales Method for Each Year')
plt.xlabel('Sales Method')
plt.ylabel('Total Operating Profit')
plt.legend(title='Year')

plt.show()


# In[37]:


#creating fig. size
plt.figure(figsize=(8, 4))

sns.barplot(x='Retailer', y='Operating_Profit', hue='Year', data=most_profitable_retailer, )
plt.title('Most Profitable Retailer for Each Year')
plt.xlabel('Retailer')
plt.ylabel('Operating Profit')
plt.legend(title='Year')


plt.show()


# In[35]:


# creating fig. size
plt.figure(figsize=(14, 8))

# heatmap vizualization 
sns.heatmap(profit_region_sales_pivot, annot=True, fmt=".2f", cmap="YlGnBu", cbar_kws={'label': 'Operating Profit'})
plt.title('Operating Profit by Region and Sales Method (2020 vs 2021)')
plt.xlabel('Year and Sales Method')
plt.ylabel('Region')
plt.show()


# In[ ]:


'''
 INSIGHTS FROM THE HEATMAP ABOVE:

1. Growth Trends: Notably, the sales figures for 2021 show significant growth compared to 2020 in most
regions and sales methods, indicating an overall improvement in sales performance for Adidas.

2. Sales Method Comparison: The data allows for analyzing which sales methods are most effective in 
different regions. For instance, In-store sales in the Midwest and Northeast regions were substantial 
in both years, while the Online sales surged in the South in 2021, indicating a shift in consumer
purchasing behavior.

3. Data Gaps: There are NaN (Not a Number) values in the data, particularly in the South for the 
In-store sales in 2020 and for the Outlet sales in the Southeast region. This might indicate either 
no sales occurred through these methods or missing data that requires further investigation.

'''


# In[36]:


# creating fig. size
plt.figure(figsize=(16, 10))

# heatmap vizualization
sns.heatmap(profit_region_retailer_pivot, annot=True, fmt=".2f", cmap="Blues", cbar_kws={'label': 'Operating Profit'})
plt.title('Operating Profit by Region and Retailer (2020 vs 2021)')
plt.xlabel('Year and Retailer')
plt.ylabel('Region')

plt.show()


# In[ ]:


'''
INSIGHTS FROM HEATMAP ABOVE:

1. Operating profit Performance: The data indicates varying performance levels across retailers and 
regions. For instance, in the Midwest, Foot Locker significantly increased its sales from 
2020 to 2021, showcasing its strength in that region.

2. Retailer Comparison: Retailers like Amazon and Walmart appear to have robust sales figures in
multiple regions, particularly in 2021, which may indicate a successful adaptation to market demands.

3. Data Gaps: NaN values suggest missing data points for certain retailer-region combinations. 
This may indicate either no sales occurred through those channels or simply incomplete records that
could be addressed for a more comprehensive analysis.

The use of the ‘Blues’ colormap in the heatmap offers a clear and engaging visual representation of 
operating profit data, making it easy to understand at a glance. looking at the varying shades of 
blue, this can quickly help in identifying which retailers and regions are thriving and which ones
might require some strategic tweaks to boost profitability. This visual tool is not just informative;
it's essential for making data-driven decisions. And also, to concentrate efforts on the areas that 
present the most potential for growth and improvement. Ultimately, this helps to drive better results 
and strengthen the product market position.

This viz. serves as a vital tool for assessing how Adidas has performed across its various retail
partners and regions, highlighting trends that could inform future sales strategies and marketing 
initiatives.


'''

