import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
 
fromaddr = "bdptma108@gmail.com"
to_addr = ['smdarknight10@gmail.com', 'ishanchoudhury1996@gmail.com', 'aniketakaruth@gmail.com']
recipients = ['mithal2424@gmail.com','rahsnh@hotmail.com']

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = ", ".join(to_addr)
msg['Subject'] = "Netflix Payment Reminder"
 
body = "Hi bros, \n\nToday is 1st. So try to pay for Netflix by today or tomorrow night, so that I can recharge on 3rd.\n\nHappy Netflix-ing!\n\n*This message is sent via an automated Python script and needs no reply*"

msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "digitalfortress")
text = msg.as_string()
server.sendmail(fromaddr, to_addr + recipients, text)
server.quit()
