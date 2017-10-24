import datetime
import random

import re
from urllib.request import urlopen

from bs4 import BeautifulSoup

pages=set()
random.seed(datetime.datetime.now())

#获取页面所有的内链列表
def getInternalLink(bsobj,includeUrl):
    internallink=[]
    for link in bsobj.findAll('a',href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs["href"] is not None:
            if link.attrs["href"] not  in  internallink:
                internallink.append(link.attrs["href"])
    return internallink
#获取页面所以得外链列表
def getExternalLink(bsobj,excludeUrl):
    externalUrl=[]
    #找出所以HTTP或WWW开头且不包含当前URL的地址
    for link in bsobj.findAll("a",href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not  None:
            if link.attrs["href"] not in externalUrl:
                externalUrl.append(link.attrs["href"])
    return externalUrl
def splitAddress(address):
    addressParts=address.replace("http://","").split("/")
    return  addressParts


def getNextExternalLink():
    pass


def getRandomExternalLink(startingPage):
    html=urlopen(startingPage)
    bsobj=BeautifulSoup(html)
    externalLink=getExternalLink(bsobj,splitAddress(startingPage)[0])
    if len(externalLink)==0:
        internalLink=getInternalLink(startingPage)
        return  getNextExternalLink(internalLink[random.randint(0,len(internalLink)-1)])
    else:
        return  externalLink[random.randint(0,len(externalLink)-1)]
def followExternalOnly(startSite):
    externalLink=getRandomExternalLink(startSite)
    print("外链是:"+externalLink)
    followExternalOnly(externalLink)

url="http://androidweekly.net/"
html=urlopen(url)
bsobj=BeautifulSoup(html)
externalLinks=getExternalLink(bsobj,url)
internalLinks=getInternalLink(bsobj,url)
for internalLink in  internalLinks:
    #print(externallink)
    print(internalLink)