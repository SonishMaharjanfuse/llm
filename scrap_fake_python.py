from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://realpython.github.io/fake-jobs/"
source = requests.get(url).text
soup = BeautifulSoup(source, "lxml")

scrapper = soup.body.find_all("div", class_="column is-half")


columns = ["title", "company", "location", "datetime"]
df = pd.DataFrame(columns=columns)

for box in scrapper:
    title = box.find("h2", class_="title is-5").text
    company = box.find("h3", class_="subtitle is-6 company").text
    location = box.find("p", class_="location").text
    datetime = box.find("time").text
    data = [title, company, location, datetime]
    df.loc[len(df)] = data

print(df)
