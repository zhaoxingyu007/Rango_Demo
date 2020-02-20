from django.urls import path
from django.conf.urls import url
from rango_Defualt import views

app_name = 'rango_Defualt'

urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('demo/',views.demo_html,name='demopage')
]
