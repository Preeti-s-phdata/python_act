import pandas as pd 

files=['product_master.csv','us_sales_2000_to_2016.csv']

file1=pd.read_csv(files[0])

file2 = pd.read_csv(files[1])
file2['Date'] = pd.to_datetime(file2['Date'])
file2['Year']=file2['Date'].dt.year
grouped_data=file2.groupby(['Year','ProductID'])[['Revenue','Units']].sum().reset_index()
# print(grouped_data)
highest_revenue_index=grouped_data.groupby('Year')['Revenue'].idxmax()
# print(highest_revenue_index)
productsid_of_high_rev = grouped_data.loc[highest_revenue_index,['Year','ProductID']]
highest_units_index= grouped_data.groupby('Year')['Units'].idxmax()
productids_of_high_quantity=grouped_data.loc[highest_units_index,['Year','ProductID']]
result = productids_of_high_quantity[~productids_of_high_quantity['ProductID'].isin(productsid_of_high_rev['ProductID'])]
# print(result)
details_of_result=result.merge(file1,on='ProductID')
final= details_of_result.join(grouped_data['Revenue'], how='left')
print(final)
# print(details_of_result.merge(grouped_data, on=('ProductID')))






# print(grouped_data['Revenue'].idxmax())
# print(grouped_data['Units'].idxmax())



# print(grouped_data)
# file2['Revenue']==grouped_data['REvenue'].max() & file2['Units'] != grouped_data['Units'].max()





# grouped_data = file2.groupby('Year')['Units'].sum().reset_index()
# print(grouped_data)