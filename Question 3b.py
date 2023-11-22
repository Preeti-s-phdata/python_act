import pandas as pd 

us_sales_data = pd.read_csv('us_sales_2000_to_2016.csv')
us_sales_data['Date'] = pd.to_datetime(us_sales_data['Date'])
us_sales_data["Year"] = us_sales_data["Date"].dt.year

highest_revenue = us_sales_data.groupby('Year')["Revenue"].sum().max()
print(highest_revenue)

lowest_revenue = us_sales_data.groupby('Year')['Revenue'].sum().min()
print(lowest_revenue)
diff_high_low = highest_revenue - lowest_revenue
print(diff_high_low)