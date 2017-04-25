'''
126的smtp服务器为host：smtp.126.com  port: 25 用户名为xxx@126.com .
注意默认126邮箱没有开启smtp功能，需要登录126网页邮箱在设置中POP3/SMTP/IMAP 设置中开启

'''

import smtplib
from email.mime.text import MIMEText

mail_host="smtp.126.com"
mail_user=input("请输入smtp帐号：")
mail_pass=input("请输入密码：")

text=input("请输入邮件内容：")
msg=MIMEText(text)

msg['From']=input("From:")
msg['To']=input("To:")
msg['Subject']=input("subject：")

smtpObj=smtplib.SMTP()
smtpObj.connect(mail_host,25)
smtpObj.login(mail_user,mail_pass)
smtpObj.send_message(msg)
print("邮件发送成功")
smtpObj.quit()
