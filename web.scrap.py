import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen as uReq
my_url="https://news.google.com/covid19/map?hl=en-IN&gl=IN&ceid=IN%3Aen&mid=%2Fm%2F03rk0"
u_client =uReq(my_url)
html=u_client.read()
Soup=Soup(html,"html.parser")
title=Soup.title
data=[]
all_rows=Soup.find_all("tr")
for row in all_rows:
    row_list=row.find_all("th")
    #col_headers=Soup.find_all("td")
    dataRow=[]
    #header_list=[]
    for cell in row_list:
        dataRow.append(cell.text)
    data.append(dataRow)
    for cell in row_list:
        dataRow.append(cell.text)
    data.append(dataRow)
data1=[]
all_column=Soup.find_all("tr")
for column in all_column:
    column_list=column.find_all("td")
    datacol=[]
    header_list=[]
    for hel in column_list:
        datacol.append(hel.text)
    data1.append(datacol)
    #df=pd.DataFrame()
#title=data[1:]
data1=data1[1:]
df=pd.DataFrame(data1)
df=pd.Dataframe(data)
print(df.head(36))