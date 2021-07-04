from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

from .task import *
from .help import *
# Create your views here.


def home(request):
    send_mail_task.delay()
    return HttpResponse("<h1>hello, from CELERY</h1>")