from bs4 import BeautifulSoup
import json, requests

def get_in_json():
    dictionary = take_html()
    return dictionary

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
        img = article.find("figure", class_="article-lead-image-wrap").get("data-original")
        link =  article.get("href").strip()
        date = article.find("time", class_="published-date relative-date").get("data-published-date")
        dictionary += [{"title": title, "autor": another_information, "discription": discription, "link": link, "img": img, "date": date, "orign": "www.space.com"}]
    return(dictionary)