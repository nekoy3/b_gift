import requests
from bs4 import BeautifulSoup

url = "https://www.sejuku.net/blog/"

response = requests.get(url)
response.encoding = response.apparent_encoding

bs = BeautifulSoup(response.text, 'html.parser')

for i in bs.select("h3"):
    print(i.getText())