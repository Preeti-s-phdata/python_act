import pandas as pd 
# import plotly.express as px


us_sales_data = pd.read_csv('us_sales_2000_to_2016.csv')
us_sales_data['Date'] = pd.to_datetime(us_sales_data['Date'])
us_sales_data["Year"] = us_sales_data["Date"].dt.year
highest_revenue = us_sales_data.groupby('Year')["Revenue"].sum().max()
print(highest_revenue)

yearlyrevediff = us_sales_data.groupby('Year')["Revenue"].sum().mean()
print(yearlyrevediff)

newsdd = highest_revenue- yearlyrevediff
print(newsdd)




# disp = px.bar(yearly_avg_salary , x='', y='Revenue')
# disp.show()
# print(yearly_avg_salary['Revenue'].min())




# print(yearly_avg_salary['Revenue'].sort_values(ascending=False))
# print(yearly_avg_salary.sort_values('Revenue', ascending=False))