import pandas as pd

us_quantity_data = pd.read_csv('us_sales_2000_to_2016.csv')
us_quantity_data['Date'] = pd.to_datetime(us_quantity_data['Date'])
# print(us_quantity_data.info())

us_quantity_data['Year'] = us_quantity_data['Date'].dt.year
# print(us_quantity_data)
us_quantity_data['Quarter'] = us_quantity_data['Date'].dt.quarter

grp_data_with_units = us_quantity_data.groupby(['Year','Quarter'])['Units'].sum().reset_index()

lowest_unit_quarter =us_quantity_data.loc[grp_data_with_units['Units'].idxmin()][['Quarter','Year']]
print(lowest_unit_quarter)