"""
python对docx的读取支持的不是很好，需要先读取为XML文件
然后对xml进行清洗
"""

from zipfile import ZipFile
from urllib.request import urlopen
from io import BytesIO
from bs4 import BeautifulSoup

wordFile=urlopen("http://pythonscraping.com/pages/AWordDocument.docx").read()
#将word都城二进制文件对象
wordFile=BytesIO(wordFile)
#解压
document=ZipFile(wordFile)
xml_content=document.read('word/document.xml')
xml=xml_content.decode('utf-8')
print(xml)

print('='*30+"获取文本内容"+'='*30)
wordObj=BeautifulSoup(xml,"lxml")
textStrings=wordObj.findAll("w:t")
#打印内容，如果时标题，插入<h1></h1>标签
for textElem in textStrings:
    closeTag=""
    try:
        style=textElem.parent.previousSibling.find("w:pstyle")
        if style is not None and style["w:val"]=="Title":
            print("<h1>")
        closeTag="</h1>"
    except AttributeError:
        #不打印标签
        pass
    print(textElem.text)
    print(closeTag)


