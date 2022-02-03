from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def greeting(req , name):
    context = {}
    context['name'] = name
    return HttpResponse('<h1>Welcome {}</h1>'.format(name))