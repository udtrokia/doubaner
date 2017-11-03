
###spider
import json
from lxml import etree
##my tool
from tools.index import *
import requests

##mongo
import pymongo
client=pymongo.MongoClient("localhost",27017)
db=client.douban

###get session
s=requests.Session()
s.headers.update({'User-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'})

info = json.load('account.json')

s.post('https://www.douban.com/accounts/login',info)

cookie="cookie: ASP.NET_SessionId=yr3bkqmsbps5xl250phjhi45"
###rootUrl
domain="https://www.douban.com/"

##getDirarys###
#rootPages=[]
#for page in range(1,31):
#    rootPages.append(domain+'?p='+str(page))
#diraryXpath='//div[@class="mod"]//div[@class="title"]//@href'
#sendPages(s,rootPages)
####

####dirary###
diraryslist=db.diraryUrls.find()
mixDirarys=[]
for l in diraryslist:
    mixDirarys.extend(l['pages'])
sendDirarys(mixDirarys)
######
