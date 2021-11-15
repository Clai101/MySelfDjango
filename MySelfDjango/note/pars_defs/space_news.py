from bs4 import BeautifulSoup
import json, requests
from functools  import reduce

def get_in_json():
    dictionary = take_html()
    return dictionary

def make_id(date):
    date = date.replace(", ",".").replace(":",".")
    date = date.split(".")
    date = list(map(int, date))
    consts = [1,1,60,24,30,12]
    id = 0
    for i in date:
        id += i*reduce(lambda x,y: x*y, consts)
        consts = consts[:-1]
    return id

def take_html():
    dictionary = []
    for i in [''] + list(map(str,list(range(2,5)))):
        url = "https://www.space.com/news/" + i
        response = requests.get(url).content
        soup = BeautifulSoup(response, 'lxml')
        di = parsin(soup)
        dictionary += di
    return dictionary


def parsin(soup):
    articles = soup.find_all("a", class_="article-link")
    dictionary = []

    for article in articles:
        title = article.find("h3", class_ = "article-name").text.strip()
        another_information = article.find("p", class_="byline").text.strip()[4:]
        discription = article.find("p", class_="synopsis").text.strip()
        try:
            img = article.find("figure", class_="article-lead-image-wrap").get("data-original")
        except:
            img = "https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Alpha%2C_Beta_and_Proxima_Centauri_%281%29.jpg/1200px-Alpha%2C_Beta_and_Proxima_Centauri_%281%29.jpg"
        link =  article.get("href").strip()
        date = article.find("time").get("data-published-date").replace("Z",'').replace("T",', ').replace("-",'.')[:-3]
        dictionary += [{"title": title, "autor": another_information, "discription": discription, "link": link, "img": img, "date": date, "orign": "www.space.com", "id": make_id(date)}]
    return(dictionary)

