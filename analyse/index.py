
###
#__init__
#analyse the data
###

#mongodb
import pymongo
#re
#my module
from plots.index import *

client=pymongo.MongoClient("localhost",27017)
db=client.douban
print('db init...')
dirarys=db.dirarys.find({}).limit(2)


#####gaPlot
#gaPlot.show(dirarys)
#####

####showWords
#wordsPlot.show(dirarys)
#print('done!')
####
