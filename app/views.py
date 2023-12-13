from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def frist(request):
    return HttpResponse('this is frist string')

def second(request):
    return HttpResponse('this is my second string')