import datetime
import time

import pandas as pd
import openpyxl

import facebookSelenium

while True:

    now = datetime.datetime.now()
    print(now)

    dataframe = pd.read_excel('./posts.xlsx', sheet_name='feed')
    doneframe = pd.read_excel('./posts.xlsx', sheet_name='done')
    print(dataframe.head())

    file = pd.ExcelFile('./posts.xlsx')
    sheets = file.sheet_names

    for sheet_name in sheets:
        print(sheet_name)



    # Convert the dataframe to an XlsxWriter Excel object.


    #doneframe = dataframe.iloc[1]

    #doneframe.to_excel(writer, sheet_name='done', index=False)

    # Close the Pandas Excel writer and output the Excel file.


    testDateTime = datetime.datetime(2021, 2, 25, 3, 0)
    print(testDateTime)

    for index, row in dataframe.iterrows():
        rowDate = datetime.datetime(row['year'], row['month'], row['day'], row['hour'], row['min'])
        if now > rowDate:
            print("Posting")
            facebookSelenium.startFBLogin(username="abryandog@gmail.com",
                                          password="And123rew456",
                                          filePath=row['photo'],
                                          message=row['text']
                                          )
            writer = pd.ExcelWriter('posts.xlsx', engine='xlsxwriter')
            doneframe = doneframe.append(row)
            dataframe = dataframe.drop(dataframe.index[index])
            dataframe.to_excel(writer, sheet_name='feed', index=False)
            doneframe.to_excel(writer, sheet_name='done', index=False)
            writer.save()


    if "Condition To post":
        print("")



        # TODO remove old post




    time.sleep(10)