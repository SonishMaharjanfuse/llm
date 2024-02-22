from bs4 import BeautifulSoup
import requests
from pprint import pprint

import pandas as pd
import time

source = requests.get("http://www.mfd.gov.np/").text

soup = BeautifulSoup(source, "lxml")

table_container = soup.body.find("div", class_="container main-body")
table = table_container.find("div", class_="highlight-box weather-data-table")

rows = table.find_all("tr")
header_row = rows[0]
columns = [th.text.strip() for th in header_row.find_all("th")]
df = pd.DataFrame(columns=columns)
for row in rows[1:-1]:
    data = [th.text for th in row.find_all("td")]
    loc = len(df)
    df.loc[loc] = data
print(df)
