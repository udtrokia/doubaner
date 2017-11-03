import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


class gaPlot:
    def show(dirarys):
        ts=[]
        [w1,w2,w3]=[[],[],[]]
        for d in dirarys:
            #time
            ts.append(d['time'][8:10])
            #three word
            pa=d['cmts']+d['ctns']
            w1.append(pa.count('时间'))
            w2.append(pa.count('尴尬'))
            w3.append(pa.count('尬聊'))
            ##df    
            df=pd.DataFrame({
                'times':ts,
                '尬':w1,
                '尴尬':w2,
                '尬聊':w3
            })
        df=df.groupby(ts).sum().sort_index(axis=1)
        df=df.cumsum()
#        df.plot()
       ###axis
        x=df.index
        y=[y1,y2,y3]=[df.iloc[:,0],df.iloc[:,1],df.iloc[:,2]]
        for n in y:
            plt.plot(x,n)

        #        
        #plot
        plt.legend(loc=1)
        plt.ylabel('次数')
        plt.xlabel(u'10月1日-10月29日')
        plt.xticks([1,6,11,16,21,26,30],[1,6,11,16,21,26,30])
        plt.title('尬,尴尬, 尬聊 在10月豆瓣热门精选日记中的出现频率～')
        #show
        plt.show()


class wordsPlot:
    def show(dirarys):
        at=np.array([])
        ac=[]

        for d in dirarys:
            pa=d['cmts']+d['ctns']
            for w in pa:
                n=ac.count(w)
                if n<1:
                    ac.append(w)

        at=np.array([0]*len(ac))
        print(at)
        for d in dirarys:
            tt=np.array([],dtype="int32")        
            for w in ac:
                tt=np.append(tt,pa.count(w))
            at=at+tt


        df=pd.DataFrame({
            'ac':ac,
            'at':at
        }).sort_values(by='at',ascending=False).head(10)
        
        df.plot()
        plt.show()

        
