import smtplib
from email.mime.text import MIMEText
msg_from="2047355787@qq.com"
passwd="bbknpfoarrncdhff"
msg_to="2047355787@qq.com"

subject="2018144143谢立东的第一次作业"
content="(wifi)ip_nat:10.101.40.151;ip:220.164.161.131;(流量)ip_nat:10.165.23.77;ip:117.136.247"
msg=MIMEText(content)
msg['Subject']=subject
msg['From']=msg_from
msg['To']=msg_to
try:
  s=smtplib.SMTP_SSL("smtp.qq.com",465)
  s.login(msg_from,passwd)
  s.sendmail(msg_from,msg_to,msg.as_string())
  print("发送成功")
except(s.SMTPException,e):
  print("发送失败")
finally:
  s.quit()