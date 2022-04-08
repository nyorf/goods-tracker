import requests
import html.parser
import time
from bs4 import BeautifulSoup

def getHtml(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.163 Mobile/15E148 Safari/604.1"
    }
    response = requests.get(url, headers=headers)
    page = BeautifulSoup(response.text, "html.parser")
    
    return page

def writePageToFile(html_page):
    file = open("page.html", "w")
    file.write(html_page.prettify())
    file.close()


if __name__ == "__main__":
    exit(0)
