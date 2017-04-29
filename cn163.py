"""
天天美剧搜索并抓取 ed2k地址
"""

from urllib.request import urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
import codecs
import re

'''
查询美剧并返回下载列表页面的url list
'''
def USTV_search(name):
    usTvName=quote(name)
    url="http://cn163.net/?s="+usTvName+"&x=-1008&y=-29"
    print("正在查询，轻稍等哦，亲。。。")
    html=urlopen(url)
    bsObj=BeautifulSoup(html,"html.parser")
    data=bsObj.findAll("div",{"class":"archive_title"})
    url=[]
    if data:
        for link in data:
            link=link.h2.a
            title=link.get_text()
            if name in title:
                print("查询到：  "+title)
                url.append(link.attrs['href'])
    else:
        print("没有查询到:"+name)
    return url

def get_ed2k(urls):
    ed2ks=""
    for url in urls:
        html=urlopen(url)
        bsObj=BeautifulSoup(html,"html.parser")
        data=bsObj.findAll('a',{'href':re.compile("ed2k")})
        for ed2k in data:
            title=ed2k.get_text()
            #后期此处添加判断是否带有字幕
            print("获取到"+title+"ed2k 资源")
            ed2ks=title+'\n'+ed2k.attrs['href']+'\n'+ed2ks
    return ed2ks

def save_ed2k(ed2ks,filename):
    with codecs.open(filename,'w','utf-8') as f:
        f.write(ed2ks)
    print("文件写入成功")
    f.close()

def main():
    usTvName=input("请输入要下载的美剧名字:")
    urls=USTV_search(usTvName)
    ed2ks=get_ed2k(urls)
    save_ed2k(ed2ks,usTvName)

if __name__=='__main__':
    main()
