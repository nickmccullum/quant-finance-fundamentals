import smtplib
import datetime

initialTime = datetime.datetime.now().strftime("%I%M%p on %B %d, %Y")
content = 'Subject: {}\n\n{}'.format('Data Feeds Builder #'+str(builderNumber)+'- Initialized', 'The data feeds builder Python script has started run at ' + initialTime)
mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()

mail.starttls()

password = ''

mail.login('support@suredividend.com',password)
mail.sendmail('support@suredividend.com','nick@suredividend.com',content)
#mail.sendmail('support@suredividend.com','ben@suredividend.com',content)

#Close the connection.
mail.close()
