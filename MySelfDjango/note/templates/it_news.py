from bs4 import BeautifulSoup
import json, requests
from note.models import News

def get_in_json():
    dictionary = take_html()
    print(dictionary)
    return dictionary
    

def last_json():
    try:
        with open(f"space_news.json", 'r') as f:
            file = json.load(f)
    except:
            file = json.loads("[]")
    return file


def take_html():
    dictionary = []
    for i in list(range(1,5)):
        url = f"https://habr.com/ru/all/page{i}/"
        response = requests.get(url).content
        soup = BeautifulSoup(response, 'lxml')
        di = parsin(soup)
        dictionary += di
    return dictionary


def parsin(soup):
    articles = soup.find_all("article", class_="tm-articles-list__item")
    dictionary = []

    for article in articles:
        title = article.find("h2", class_ = "tm-article-snippet__title tm-article-snippet__title_h2").text.strip()
        discription = article.find("div", class_="article-formatted-body article-formatted-body_version-1").text.strip()
        another_information = article.find('a', class_="tm-user-info__username").text
        img = article.find("div", class_="article-formatted-body article-formatted-body_version-1").find("img").get("src")
        link =  article.find('a', class_="tm-article-snippet__readmore").get("href").strip()
        date = article.find("time").get("title").replace('-','.')
        dictionary += [{"title": title, "autor": another_information, "discription": discription, "link": link, "img": img, "date": date, "orign": "habr.com"}]
    return(dictionary)

get_in_json()