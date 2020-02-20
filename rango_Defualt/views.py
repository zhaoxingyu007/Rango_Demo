from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return HttpResponse(r'''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Rango</title>
    </head>
    
    <body>
    <section><h1> 一个HTML的例子--用String 返回
     </h1>
        <div> <span> 这是一个html的例子</span><span> 来试试什么是inline 和 block element</span></div> <div> inline 元素会自动'合并' ， 而block会叠加</div>
        <h2> 如果两个inline元素之间有一个block元素呢？</h2>
          <div> <span> 这是一个html的例子</span> <div>我是block</div> <span> 来试试什么是inline 和 block element</span></div>
    </section>
    </body>
    </html>''')


def demo_html(request):
    return render(request, 'rango_Defualt/demo_html.html')