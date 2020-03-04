from django.urls import path
from django.conf.urls import url
from rango_Defualt import views

app_name = 'rango_Defualt'

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('pic/', views.re_sikiro, name='pic'),
]
