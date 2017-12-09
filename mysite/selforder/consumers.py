import json
import time

from django.core.mail import send_mail
from channels.channel import Group



def send_email_consumer(message):
    payload = message.content['payload']
    send_mail(payload['subject'], payload['body'], 'root@localhost', [payload['email']],
              fail_silently=False)
