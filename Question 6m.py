import pandas as pd

usa_sales_data_extract = pd.read_csv("us_sales_2000_to_2016.csv")
products_sales_data = pd.read_csv("product_master.csv")
zip_master_sales_data = pd.read_csv("zip_usa_master.csv")

fort_worth_data = zip_master_sales_data[zip_master_sales_data["PlaceName"] == "Fort Worth"]
print(fort_worth_data)
joined_data_has_fw = fort_worth_data.join(usa_sales_data_extract, how="left")
print(joined_data_has_fw)
most_sold_product = joined_data_has_fw.groupby("ProductID")["Units"].sum().idxmax()
print(most_sold_product)

famous_product_name = products_sales_data.loc[products_sales_data["ProductID"] == most_sold_product, "Product"].values[0]
print(famous_product_name)

