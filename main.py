import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://en.wikipedia.org/wiki/Main_Page"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

headers = []

for header in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
    text = header.text.strip()
    level = header.name
    headers.append((text, level))

df = pd.DataFrame(headers, columns=["Text", "Level"])
print(df)
