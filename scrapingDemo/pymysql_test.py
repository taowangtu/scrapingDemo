#!-*-coding:utf-8 -*-
import pymysql
conn=pymysql.connect(host='127.0.0.1',user='root',passwd='111111',db='scraping',charset='utf8')
cur=conn.cursor()
cur.execute("INSERT INTO pages(title)VALUES('测试中文');")
cur.connection.commit()
cur.close()
conn.close()
