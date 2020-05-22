import requests
from bs4 import BeautifulSoup as bs
import socket


def makeRequest(key):
    try:
        response = requests.get(f"https://www.youtube.com/watch?v={key}")
        print("[REQUEST] 172.217.164.142")
        if response.status_code != 200:
            raise Exception
        html = response.text
        return(html)
    except Exception:
        print("Something went wrong...")
        print("Check the Video URL")


def findViewsInHTML(text):
    soup = bs(text, "html.parser")
    views = int(soup.find("div", attrs={"class": "watch-view-count"}).text[:-6].replace(",", ""))
    return(views)

def findVidTitle(text):
    soup = bs(text, "html.parser")
    title = soup.find("span", attrs={"class": "watch-title"}).text.strip()
    return(title)

def main(key):
    html_text = makeRequest(key)
    currentViews = findViewsInHTML(html_text)
    return(currentViews)