import pandas as pd


usa_sales = pd.read_csv("us_sales_2000_to_2016.csv")
products = pd.read_csv("product_master.csv")
usa_master = pd.read_csv("zip_usa_master.csv")

usa_sales["Date"] = pd.to_datetime(usa_sales["Date"])
usa_sales['Year'] = usa_sales['Date'].dt.year
filter_data_set = usa_sales[(usa_sales["Year"] == 2015) | (usa_sales["Year"] == 2016)]

merged_data_set = pd.merge(filter_data_set, usa_master, left_on="Zip", right_on="PostalCode", how="left")
# print(merged_data_set)

total_units_2015_2016 = merged_data_set.groupby(["Year", "PlaceName"])["Units"].sum()
area_result = total_units_2015_2016.groupby('Year',group_keys=False).apply(lambda x: x.nsmallest(10)).reset_index()
print(area_result)


