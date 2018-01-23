# 抓取['尬', '尴尬', '尬聊']在豆瓣近一月热门精选中出现的频率



## 导语

_昨天害了朋友尬聊, 突然有想法爬一下['尬', '尴尬', '尬聊']在豆瓣近一月热门精选中出现的频率_



## 网页版豆瓣

### route

思路的话就是: 

​	pages -> dirary 

​				=> get content

​				=> get comment

### URL

_热门精选涵盖了本月的热门日记(25,Oct-2,Oct)_



第一页是`www.douban.com`

第二页是`www.douban.com?p=2`

...

第三十二页是`www.douban.com?p=32`



### Frame

#### 列表页结构

+ 日记列表 `class="stream-items"`
+ 单个日记 `class="new-status status-wrapper"`
+ 日记标题 `class="hd"`
  + 用户头像 `class="usr-pic"`
  + 标题文本 `class="text"`
+ 日记内容 `class="bd editer"`
  + 内容图片 `class="pic"`
  + 内容文本 `class="content"`
    + 文本标题 `class="title"`

#### 日记页结构

从列表内的单个日记的链接可以跳转到日记页

+ 日记内容

+ 评论区

  _评论的结构控制台看不出来, 不过这难不倒我们, 我们直接把整个页面抓取下来_