import smtplib


class SendMail:
    def __init__(self, subject, body, recipient):
        self.subject = subject
        self.body = body
        self.recipient = recipient

    def mail_send(self):
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        message = 'Subject: {}\n\n{}'.format(self.subject, self.body)

        s.starttls()

        s.login("achandil86@gmail.com", "ppuiphtpiruewpog")

        # sending the mail
        s.sendmail('achandil86@gmail.com', self.recipient, message)

        # terminating the session
        s.quit()


if __name__ == '__main__':
    subject = input("Enter Subject:- ")
    body = input("Enter Body:- ")
    recipient = input("Enter recipient:- ")
    obj = SendMail(subject, body, recipient)
    obj.mail_send()
