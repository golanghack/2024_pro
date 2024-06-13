from celery import shared_task
from django.core.mail import EmailMessage

@shared_task
def send_email(owner_name, order_name, owner_email):
    mail_subject = 'order ready'
    message = f'Hello {owner_name}, your order ready {order_name}'
    email = EmailMessage(mail_subject, message, to=[owner_email])
    email.send()