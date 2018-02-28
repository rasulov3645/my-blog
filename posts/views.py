from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


# home page
def index(request):
    context = {'text': 'Hello world!'}
    return render(request, 'base.html', context)


# home page
# def home(request):
#     context = '<h1>Hello world!</h1>'
#     return HttpResponse(context)



# def index(request):
#     if request.method == 'GET':
#         return HttpResponse('Запрос получен!')
#     elif request.method == 'POST':
#         return HttpResponse('Запрос опубликован!')
