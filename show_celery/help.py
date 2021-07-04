from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

from .task import *
# Create your views here.

def send_mail_without_celery():
    send_mail('Celery just worked', "Celery done",
              "usernasim272727@gmail.com",
              ['nasimnasimnasim272727@gmail.com'],
              fail_silently= False
              )
    return None