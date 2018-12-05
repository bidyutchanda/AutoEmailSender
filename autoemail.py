import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
 
fromaddr = "YOUR OWN EMAIL ID"
to_addr = ['EMAIL ID 1', 'EMAIL ID 2']
recipients = ['EMAIL ID 3','EMAIL ID 4']

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = ", ".join(to_addr)
msg['Subject'] = "SUBJECT OF EMAIL"
 
body = "EMAIL TEXT"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "YOUR EMAIL PASSWORD")
text = msg.as_string()
server.sendmail(fromaddr, to_addr + recipients, text)
server.quit()
