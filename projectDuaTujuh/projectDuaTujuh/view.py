from django.shortcuts import render

def index(request):
    content= {
        'judul':'Home'
    }
    return render(request,'index.html',content)