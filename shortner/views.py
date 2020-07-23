from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def url_redirect(request):
    return HttpResponse('Hello')