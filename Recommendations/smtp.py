from email.message import EmailMessage
import ssl
import smtplib
import json

class ManagingMails:

    def sendMail(self, data):

        # Formatting the data
        data_formatted = json.dumps(data)

        sent_from = 'nbanotifierscraper@gmail.com'
        senderPassword = 'rlemdemqeqfjocix'
        to = 'aashishbisht01@gmail.com'
        subject = 'Last Week NBA Recap'
        body = f"""
        Heyoo here's the week recap of NBA
        
        {data_formatted}
        """
        em = EmailMessage()
        em['From'] = sent_from
        em['To'] = to
        em['Subject'] = subject
        em.set_content(body)
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sent_from, senderPassword)
            smtp.sendmail(sent_from, to, em.as_string())