"""
本模块可以将任意的pdf文件读成字符串，然后利用StringIO转换成文件对象
"""

from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager,process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open

def readPDF(pdfFile):
    rsrcmgr=PDFResourceManager()
    retstr=StringIO()
    laparams=LAParams()
    device=TextConverter(rsrcmgr,retstr,laparams=laparams)

    process_pdf(rsrcmgr,device,pdfFile)
    device.close()

    content=retstr.getvalue()
    retstr.close()
    return content

pdfFile=urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
#readPDF()也可以读取本地pdf文件
#pdfFile=open("本地文件","rb")
outputString=readPDF(pdfFile)
print(outputString)
pdfFile.close()
