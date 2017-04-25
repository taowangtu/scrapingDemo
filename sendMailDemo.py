"""
sendMail(subject,body)为发送邮件模块。
此程序，每小时检查一次https://isitchristmas.com/ 网站，如果页面信息不是“不是”，则这天就是圣诞节。
发邮件告诉你圣诞节到啦

"""

import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time

def sendMail(subject,body):
    msg=MIMEText(body)
    msg['Subject']=subject
    msg['From']="xxx@xxx.xxx"
    msg['To']="xxx@xxx.xxx"
    
    mail_host="smtp.126.com"
    mail_user="xxx@xxx.xxx"
    mail_pass=""
    smtpObj=smtplib.SMTP()
    smtpObj.connect(mail_host,25)
    smtpObj.login(mail_user,mail_pass)
    smtpObj.send_message(msg)

bsObj=BeautifulSoup(urlopen("https://isitchristmas.com/"), "lxml")

while(bsObj.find("a",{"id":"answer"}).attrs['title']=="IFTTT"):
    print("It is not Christmas yet.")
    time.sleep(3500)
    bsObj=BeautifulSoup(urlopen("https://isitchristmas.com/"),"lxml")
sendMail("It's Christmas!","According to http://itischristmas.com,it is Christmas!")

