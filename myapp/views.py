from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('is good man')

def detail(request,num):
    return HttpResponse('detail-%s'%num)
