import requests
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com")
soup = BeautifulSoup(response.content, "html.parser")

for post in soup.select('.text'):
    print(post.text)

