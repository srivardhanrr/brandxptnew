from django.core.mail import EmailMessage
import threading


class EmailManager(threading.Thread):
    def __init__(self, settings):
        self.settings = settings
        threading.Thread.__init__(self)

    def send_email(self, subject, body, recipient_list, from_email=None):
        email = EmailMessage(
            subject,
            body,
            from_email or self.settings.EMAIL_HOST_USER,
            recipient_list,
        )
        threading.Thread(target=email.send).start()