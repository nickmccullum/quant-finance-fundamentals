import pandas as pd
 
tgt_website = r'https://sg.finance.yahoo.com/quote/WDC/key-statistics?p=WDC'
 
def get_key_stats(tgt_website):
 
    # The web page is make up of several html table. By calling read_html function.
    # all the tables are retrieved in dataframe format.
    # Next is to append all the table and transpose it to give a nice one row data.
    df_list = pd.read_html(tgt_website)
    result_df = df_list[0]
 
    for df in df_list[1:]:
        result_df = result_df.append(df)
 
    # The data is in column format.
    # Transpose the result to make all data in single row
    return result_df.set_index(0).T
 
# Save the result to csv
result_df = get_key_stats(tgt_website)
