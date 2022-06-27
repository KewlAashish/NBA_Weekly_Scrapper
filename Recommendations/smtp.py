from email.message import EmailMessage
import ssl
import smtplib

class ManagingMails:

    def sendMail(self, data):



        sent_from = 'nbanotifierscraper@gmail.com'
        senderPassword = 'rlemdemqeqfjocix'
        to = 'aashishbisht01@gmail.com'
        subject = 'Last Week NBA Recap'
        body = f"""
        Heyoo here's the week recap of NBA
        
        {data}
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