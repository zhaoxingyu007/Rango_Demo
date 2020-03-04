from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return HttpResponse('Welcome to rango')


def demo_html(request):
    return render(request, 'rango_Defualt/demo_html.html')

def re_sikiro(request):
    return HttpResponse("<img src='/media/sikiro.png'>")