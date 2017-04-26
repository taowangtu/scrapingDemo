"""
从网络中直接读取csv文件
"""

from urllib.request import urlopen
from io import StringIO
import csv

#转义字符因为不能被ascii decode，如果不加ignore就会报错，加了ignore就会被忽略
data=urlopen("http://pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii','ignore')
dataFile=StringIO(data)
#读取为列表对象
csvReader=csv.reader(dataFile)
#读取位字典对象,把每一行转换成python的字典对象，并把字段列表保存在变量dictReader.fieldnames中
dictReader=csv.DictReader(dataFile)
print(dictReader.fieldnames)

for row in csvReader:
    print(row)
    print("The album \""+row[0]+"\" was released in "+str(row[1]))

for row in dictReader:
    print(row)
