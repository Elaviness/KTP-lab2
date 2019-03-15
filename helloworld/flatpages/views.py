#coding:utf-8

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse(u'Привет, Мир!')
    return render(request, 'static_handler.html', {})
