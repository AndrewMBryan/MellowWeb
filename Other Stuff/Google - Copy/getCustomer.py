





import requests, json
import pandas as pd
import openpyxl
import xlrd

df = pd.read_excel('fulltest.xlsx', sheet_name='Sheet1')

print(df)

#print(df[df['types'] == 'roofing_contractor'])

for index, rows in df.iterrows():
    types = rows['types']
    #print(types)
    if 'roofing_contractor' in types:
        #print('inside')
        print()
    else:
        df = df.drop(index)
print(df)

df.to_excel('cleaned.xlsx')