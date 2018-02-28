from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# home page
def home(request):
    context = '<h1>Hello world!</h1>'
    return HttpResponse(context)
