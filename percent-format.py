import pandas as pd

# Create a Pandas dataframe from the data.
df = pd.DataFrame({'Data': [10, 20, 30, 20, 15, 30, 45]})

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Get the xlsxwriter objects from the dataframe writer object.

workbook  = writer.book
worksheet = writer.sheets['Sheet1']
percentageFormat = workbook.add_format({'num_format': '0.0%'})
worksheet.set_column('B:B', None, percentageFormat)

writer.save()
