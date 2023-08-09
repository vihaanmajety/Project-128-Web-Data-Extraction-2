from bs4 import BeautifulSoup
import pandas as pd
import requests

url="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page=requests.get(url)
soup=bs(page.text,"html.parser")
star_table=soup.find_all("table",{"class":"wikitable sortable"})
total=len(star_table)
temp_list=[]
table_rows=star_table.find_all("tr")
for tr in table_rows:
    td=tr.find_all("td")
    row=[i.text.rstrip() for i in td]
    temp_list.append(row)

star_names=[]
distance=[]
mass=[]
radius=[]
lum=[]
for i in range(1,len(temp_list)):
    star_names.append(temp_list[i][1])
    distance.append(temp_list[i][3])
    mass.append(temp_list[i][5])
    radius.append(temp_list[i][6])
    lum.append(temp_list[i][7])



headers=["star_names","distance","mass","radius","luminosity"]

star_df_2= pd.DataFrame(list(zip(star_names,distance,mass,radius,luminosity)), columns=headers)


star_df_2.to_csv('scraped_data.csv',index=True, index_label="id")