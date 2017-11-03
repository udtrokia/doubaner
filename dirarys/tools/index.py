##mongo
import pymongo
client=pymongo.MongoClient("localhost",27017)
db=client.douban

#import
import requests
import time
from lxml import etree
import random

# get dirary list 

def analysePage(s,page,index):
    r=s.get(page)
    html=etree.HTML(r.text)

    ctnXpath='//div[@class="mod"]//div[@class="title"]//@href'
    ctn=html.xpath(contentXpath)
    
    db.diraryUrls.insert({'page':index,'urls':ctn})
    
def sendPages(s,pages):
    for index,page in enumerate(pages):
        analysePage(s,page,index)
        rdm=random.randint(1,6)        
        time.sleep(rdm)
        print("insert page%d to mongodb success \nsleep...%d"%(index,rdm))        

# get article content && comment
def analyseDirary(dirary):
    res=requests.get(dirary)
    html=etree.HTML(res.text)
    try:
        titleXpath='//div[@class="note-header note-header-container"]//h1'
        timeXpath='//span[@class="pub-date"]'
        ctnXpath='//div[@class="note"]//p'
        cmtXpath='//div[@id="comments"]//p'

        title=html.xpath(titleXpath)[0].text
        t=html.xpath(timeXpath)[0].text
        article=html.xpath(ctnXpath)
        comment=html.xpath(cmtXpath)
        ctns=''

        for pa in article:
            ctns+=str(pa.text)
            cmts=''

        for pa in comment:
            cmts+=str(pa.text)

        detail={'title':title,'time':t,'ctns':ctns,'cmts':cmts}
        db.dirarys.insert(detail)
        ##sleep for a while
        rdm=random.randint(1,5)
        time.sleep(rdm)
        print('analyse dirary success! sleep %ss...'%str(rdm))
    except:
        print('this is note dirary jump to next')

def sendDirarys(dirarys):
    listlen=len(dirarys)
    for index,dirary in enumerate(dirarys):
        analyseDirary(dirary)
        rdm=random.randint(1,5)
        time.sleep(rdm)
        index=index+1
        print('insert dirary to mongodb finish %d/%d sleep %ss...'%(index,listlen,str(rdm)))



