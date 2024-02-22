from bs4 import BeautifulSoup
import requests
import pandas as pd

columns = ["quote", "author", "tags"]
df = pd.DataFrame(columns=columns)

for page in range(10):
    url = f"https://quotes.toscrape.com/page/{page}"

    source = requests.get(url).text
    soup = BeautifulSoup(source, "lxml")

    # print(soup.prettify())

    scrapper = soup.find_all("div", class_="quote")

    # print(scrapper)

    for box in scrapper:
        quotes = box.find("span", class_="text").text
        author = box.find("small", class_="author").text
        tags = box.find("div", class_="tags").text
        data = [quotes, author, tags]
        df.loc[len(df)] = data

print(df)
