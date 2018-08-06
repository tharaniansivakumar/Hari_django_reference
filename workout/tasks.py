import time
import os
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.utils.crypto import get_random_string

from celery import shared_task

from myproject.settings import PROJECT_ROOT


@shared_task()
def add(value):
    print(value)
    for i in range(10):
        time.sleep(3)
        print(i)

@shared_task()
def ml(value):
        print("Entered")
        print(value)
        time.sleep(value)
        count=0
        with open(os.path.join(PROJECT_ROOT, 'task.txt')) as f:
            to = f.readline().strip()
            val = to.split(',')
            # return HttpResponse(len(val))
            subject = f.readline().strip()
            content = f.read()
            if (len(val) == 1):
                email = EmailMessage(subject, content, to=[to])
            else:
                email = EmailMessage(subject, content, to=val)
            if (email.send()):
                count+=1
                print("success")
            else:
                print("Failed")