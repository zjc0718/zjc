import urllib2
import re
url = "http://www.gushiwen.org/gushi/tangshi.aspx"
data = urllib2.urlopen(url).read().decode("utf-8","ignore")
pat = re.compile('<span><a href="(.*?)"',re.S)
rst = re.findall(pat,data)
for i in range(0,len(rst)):
    url2 = rst[i]
    data2 = urllib2.urlopen(url2).read().decode("utf-8","ignore")
    pat2 = re.compile('<textarea style=" .*?>(.*?)h',re.S)
    rst2 = re.findall(pat2,data2)
    rst3 = rst2[0].encode("utf-8")
    print rst3
    print '\n'
    if (i+1)%5 == 0:
        input = raw_input()
        if input == '':
            continue
        else:
            break