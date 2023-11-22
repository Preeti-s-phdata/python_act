import pandas as pd
import plotly.express as px

sales_data = pd.read_csv('us_sales_2000_to_2016.csv')
sales_data_copy = sales_data.copy(deep=True)
# sales_data.info()

# print(sales_data)

sales_data["Date"] = pd.to_datetime(sales_data["Date"])
# sales_data.info()

sales_data["Year"] = sales_data["Date"].dt.year
# print(sales_data)

yearly_sales = sales_data.groupby("Year")["Revenue"].sum().reset_index()
# print(yearly_sales)

yearly_sales['YoY Growth'] = yearly_sales['Revenue'].pct_change() * 100
yearly_sales['YoY Growth']=yearly_sales['YoY Growth'].fillna(100)
print(yearly_sales)

# fig = px.bar(yearly_sales, x='Revenue', y='YoY Growth', title="Yearly Sales of the Client").update_layout(
#     xaxis_title="Year", yaxis_title="Year on year growth in percentage"
# )
# fig.show()


# df = pd.DataFrame(file)


# print(df.columns)
# df["Year"]= df.Date.str.split('-', expand=True)[0]
# df["Yearformat"]= pd.to_datetime(df["Date"]).dt.quarter
# df["Year"] = df["Yearformat"].
# print(df)
# print(df.groupby('Yearformat')["Revenue"].sum())

# grpfile = file.groupby(['ProductID']).count()

# print(grpfile)