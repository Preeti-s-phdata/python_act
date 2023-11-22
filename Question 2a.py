import pandas as pd
import plotly.express as px

us_sales_data_toget_quarter = pd.read_csv('us_sales_2000_to_2016.csv')

us_sales_data_toget_quarter["Date"] = pd.to_datetime(us_sales_data_toget_quarter['Date'])

us_sales_data_toget_quarter["Year"] = us_sales_data_toget_quarter['Date'].dt.year

# print(us_sales_data_toget_quarter)

us_sales_data_toget_quarter["Quarter"] = us_sales_data_toget_quarter['Date'].dt.quarter

# print(us_sales_data_toget_quarter)

grouped_data = us_sales_data_toget_quarter.groupby(['Year','Quarter'])["Revenue"].sum().reset_index()
# print(grouped_data)
grouped_data['Quaterly_Change']=grouped_data['Revenue'].pct_change() * 100
grouped_data['Quaterly_Change'] = grouped_data['Quaterly_Change'].fillna(100)
print(grouped_data)

# disp = px.bar(grouped_data, x="Quaterly_Change", y="Year")
# disp.show()