from bs4 import BeautifulSoup
import time
import actions

def tracking(url):
    while True:
        page = actions.getHtml(url)
        availability = isAvailable(page)
        if availability:
            file = open("result.txt", "w")
            file.write('Товар появился в наличии.')
            file.close()
        time.sleep(10)

def isAvailable(html_page):
    result = str(html_page.find("span", class_="zi6"))
    if 'Нет в наличии' in result:
        return False
    else:
        return True

if __name__ == '__main__':
    url = input('Enter Ozon item URL: ')
    page = actions.getHtml(url)
    tracking(url)
