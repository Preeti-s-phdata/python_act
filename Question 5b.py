import pandas as pd 

revenue_data = pd.read_csv('us_sales_2000_to_2016.csv')
revenue_data['Date'] = pd.to_datetime(revenue_data['Date'])

revenue_data['Year'] = revenue_data['Date'].dt.year

revenue_data['Quarter'] = revenue_data['Date'].dt.quarter

grouped_reveue_basedon_quarter = revenue_data.groupby(['Year','Quarter'])['Revenue'].sum().reset_index()

print(grouped_reveue_basedon_quarter.loc[grouped_reveue_basedon_quarter['Revenue'].idxmin()][['Year','Quarter']].astype(int))