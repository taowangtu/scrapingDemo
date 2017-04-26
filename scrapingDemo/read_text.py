"""
对于网页内容时纯文本格式的页面可以直接使用本例来读取
"""
from urllib.request import urlopen

textPage=urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt").read()
text=str(textPage,"utf-8")
print(text)
