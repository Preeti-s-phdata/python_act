import pandas as pd 
import plotly.express as px

us_sales_data = pd.read_csv('us_sales_2000_to_2016.csv')

us_sales_data["Date"] = pd.to_datetime(us_sales_data['Date'])
# us_sales_data.info()

us_sales_data["Year"] = us_sales_data["Date"].dt.year
# print(us_sales_data)

yearly_units = us_sales_data.groupby('Year')["Units"].sum().reset_index()
# print(yearly_units)
yearly_units['YoY Growth'] = yearly_units['Units'].pct_change() * 100
yearly_units['YoY Growth']=yearly_units['YoY Growth'].fillna(100)
print(yearly_units)



# disp = px.bar(yearly_units , x='Units', y='YoY Growth')
# disp.show()

# print(us_sales_data.isnull().sum().sum())

