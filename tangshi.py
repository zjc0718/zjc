#本程序实现的功能是爬取唐诗三百首，并存在本地的TXT文件中。

#导入相应的模块
import urllib.request
import re

#访问唐诗三百首的服务器，并使用正则表达式爬取每首古诗的链接。
url = "http://www.gushiwen.org/gushi/tangshi.aspx"
data = urllib.request.urlopen(url).read().decode("utf-8", "ignore")
pat = '<span><a href="(.*?)"'
rst = re.compile(pat, re.S).findall(data)

#打开一个本地文件目录，用于存放爬取的古诗。
fh = open("D:/test1/gushi.txt", "w")
#依次访问每首古诗的链接，并使用正则表达式抓取古诗内容
for i in range(0,len(rst)):
    url_0 = rst[i]
    data_0 = urllib.request.urlopen(url_0).read().decode("utf-8", "ignore")
    pat_0 = '<div class="left">.*?<div style=".*?">.*?<textarea style=".*?">(.*?)h'
    gushi = re.compile(pat_0, re.S).findall(data_0)
    #将爬取到的古诗写入本地文件。
    fh.write(gushi[0]+"\n\n")
    print("正在写入...")
#最后关闭文件。
fh.close()
print("写入完成！！！")
