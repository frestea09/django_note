from django.shortcuts import render

def index(request):
    content = {
        'judul':'Home',
        'article':'Welcome to home',
        'menu':[
            ['/','Home'],
            ['blog/','Blog'],
        ],

    }
    return render(request,'index.html',content)
