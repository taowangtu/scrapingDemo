"""
使用BeautifulSoup和python3.x对文档进行utf-8编码
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen

bsObj=BeautifulSoup(urlopen("https://en.wikipedia.org/wiki/Python"),"lxml")
content=bsObj.find("div",{"id":"mw-content-text"}).get_text()
content=bytes(content,"UTF-8")
content=content.decode("utf-8")
print(content)
