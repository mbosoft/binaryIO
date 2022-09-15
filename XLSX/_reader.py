# pip install xlrd
# pip install pandas

import pandas as pd
dataframe = pd.read_excel('sample_workbook.xlsx', sheet_name='ss')
print(dataframe)
