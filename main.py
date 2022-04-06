import requests
import html.parser
import time
from bs4 import BeautifulSoup


def getHtml(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/87.0.4280.163 Mobile/15E148 Safari/604.1"
    }
    
    response = requests.get(url, headers=headers).text
    page = BeautifulSoup(response, "html.parser")
    
    return page

def isAvailable(html_page):
    result = str(html_page.find("span", class_="zi6"))
    if 'Нет в наличии' in result:
        return False
    else:
        return True
    #return html_page.prettify()

def writePageToFile(html_page):
    file = open("page.html", "w")
    file.write(html_page.prettify())
    file.close()

def tracking(url):
    while True:
        page = getHtml(url)
        availability = isAvailable(page)
        if availability:
            file = open("result.txt", "w")
            file.write('Товар появился в наличии.')
            file.close()
        time.sleep(10)


if __name__ == "__main__":
    url = input("Enter Ozon item page URL: ")
    page = getHtml(url)
    tracking(url)
