import datetime
import random
from urllib.request import urlopen

import re
from bs4 import BeautifulSoup
from requests import HTTPError
def getLinks(article):
    url = "http://en.wikipedia.org" + article
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsobj = BeautifulSoup(html)
        # title=bsobj.body.div.get_text()
    except AttributeError as e:
        return None
    return bsobj.find("div",{"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))
def getLink_All(article):
    global pages
    url = "http://en.wikipedia.org" + article
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsobj = BeautifulSoup(html)
        print(bsobj.find(id="mw-content-text").findAll("p")[0])
        print(bsobj.h1.get_text())
        print(bsobj.find(id="ca-edit").find("span").find("a").attrs['href'])
        # title=bsobj.body.div.get_text()
    except AttributeError as e:
        return None
    for link in bsobj.findAll("a",href=re.compile("^(/wiki/)")):
        if "href" in link.attrs:
            if link.attrs["href"] not in pages:
                #我们遇到新页面
                newPage=link.attrs["href"]
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)
article="/wiki/Kevin_Bacon"
pages=set()
getLink_All(article)
'''
link_All=getLinks(article)
#random.seed(datetime.datetime.now())
if link_All==None:
    print("title could not be found")
else:
   while len(link_All)>0:
       newArticle=link_All[random.randint(0,len(link_All)-1)].attrs["href"]
       print(newArticle)
       link_All=getLinks(newArticle)
'''