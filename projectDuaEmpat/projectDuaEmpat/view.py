from django.shortcuts import render

def index(request):
    content={
        'sectionWeb':'Home',
        'judul':'Home',
        'article':'Selamat Datang di home',
    }
    return render(request,'index.html',content)