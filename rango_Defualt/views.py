from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'rango_Defualt/homepage.html')

def re_sikiro(request):
    return HttpResponse("<img src='/media/sikiro.png'>")

def about(request):
    return render(request, 'rango_Defualt/about.html' )