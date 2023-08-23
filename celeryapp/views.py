from django.shortcuts import render
from .tasks import fun
from django.http import HttpResponse
from mailfireapp.tasks import send_mail_func

# Create your views here.

def testView(request):
    fun.delay()
    return HttpResponse("Done")

def send_mail_to_all_users(request):
    send_mail_func.delay()
    return HttpResponse("Email has beed Sent Successfully")