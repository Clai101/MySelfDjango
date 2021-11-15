from bs4 import BeautifulSoup
import json, requests
from functools  import reduce

def it_get_in_json():
    dictionary = it_take_html()
    return dictionary

def it_take_html():
    dictionary = []
    url = f"https://habr.com/ru/all/"
    response = requests.get(url).content
    soup = BeautifulSoup(response, 'lxml')
    di = it_parsin(soup)
    dictionary += di
    for i in range(2,5):
        url = f"https://habr.com/ru/all/page{i}/"
        response = requests.get(url).content
        soup = BeautifulSoup(response, 'lxml')
        di = it_parsin(soup)
        dictionary += di
    return dictionary

def it_make_id(date):
    date = date.replace(", ",".").replace(":",".")
    date = date.split(".")
    date = list(map(int, date))
    consts = [1,1,60,24,30,12]
    id = 0
    for i in date:
        id += i*reduce(lambda x,y: x*y, consts)
        consts = consts[:-1]
    return id

def it_parsin(soup):
    articles = soup.find_all("article", class_="tm-articles-list__item")
    dictionary = []

    for article in articles:
        try:
            title = article.find("a", class_="tm-article-snippet__title-link").text.strip()
            discriptions = article.find_all("p")
            discription = ""
            for i in discriptions:
                discription += i.text.strip() + "\n"
            another_information = article.find('a', class_="tm-user-info__username").text
            img = None
            try:
                img = articlefind("img", class_ = "tm-article-snippet__lead-image").get("src")
            except:
                try:
                    img = article.find("div", class_="tm-article-body tm-article-snippet__lead").find("img").get("src")   
                except:
                    try:
                        img = article.find("div", class_="article-formatted-body article-formatted-body_version-1").find("img").get("src")
                    except:
                        img = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Alpha%2C_Beta_and_Proxima_Centauri_%281%29.jpg/1200px-Alpha%2C_Beta_and_Proxima_Centauri_%281%29.jpg"
            link =  article.find('a', class_="tm-article-snippet__title-link").get("href").strip()
            date = article.find("time").get("title").replace('-','.')
            dictionary += [{"title": title, "autor": another_information, "discription": discription, "link": link, "img": img, "date": date, "orign": "https://habr.com", "id":it_make_id(date)}]
        except:
            pass
    return(dictionary)