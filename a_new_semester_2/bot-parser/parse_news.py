import requests
from bs4 import BeautifulSoup

def parse_default_news(date=None):
    links = []
    result = []
    if not date:
        response = requests.get("https://www.pravda.com.ua/news/")
        soup =  BeautifulSoup(response.content, "html.parser")

        headers = soup.select(".article_header > a")
        for link in headers[:3]:
            l = link.get("href")
            links.append(l)

if __name__ == "__main__":
    print(parse_default_news())
