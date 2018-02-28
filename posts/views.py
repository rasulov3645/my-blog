from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views import View

# home page
def index(request):
    context = {'text': 'Hello world!'}
    return render(request, 'base.html', context)


class Index(View):
    """
    class Index
    """

    #get запрос
    def get(self, request):
        return HttpResponse('Запрос получен!')

    # post запрос
    def post(self, request):
        return HttpResponse('Запрос опубликован!')



# home page
# def home(request):
#     context = '<h1>Hello world!</h1>'
#     return HttpResponse(context)



# def index(request):
#     if request.method == 'GET':
#         return HttpResponse('Запрос получен!')
#     elif request.method == 'POST':
#         return HttpResponse('Запрос опубликован!')
