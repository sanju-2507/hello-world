import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

'''
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
  
# Authentication
s.login("maheshwarisanjana007@gmail.com", "jxcjvvpalrzqmpgw")
  
message =  """<html>
                        <head></head>
                            <body>
                                <h1>Welcome to Gammastack</h1>
                                <h2>Mail Sent Successfully</a></h2>
                             
                            </body>
                        </html>
                    """
  
s.sendmail("maheshwarisanjana007@gmail.com", "sanjanamaheshwari25@gmail.com", message)
  
s.quit()
'''
me = "maheshwarisanjana007@gmail.com"
you = input("Enter reciever's email:")
msg = MIMEMultipart('alternative')
msg['Subject'] = "Gammastack"
msg['From'] = me
msg['To'] = you
html = """<html>
            <head></head>
                <body>
                    <h1>Welcome to Gammastack</h1>
                    <h2>Mail Sent Successfully</a></h2>
                 
                </body>
            </html>
        """
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls() 
s.login("maheshwarisanjana007@gmail.com", "jxcjvvpalrzqmpgw") 

part2 = MIMEText(html, 'html')

msg.attach(part2)

#attachment
filename = "demo.txt"
attachment = open("demo.txt", "rb")
p = MIMEBase('application', 'octet-stream')
p.set_payload((attachment).read())
encoders.encode_base64(p)
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(p)

s.sendmail(me,you, str(msg)) 
s.quit() 
print("mail send successfully....")
