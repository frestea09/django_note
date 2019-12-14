from django.shortcuts import render

def index(request):
    content = {
        'judulWeb':'Home',
        'judul':'Home',
        'article':'Selamat Datang, ini adalah halaman home'
    }
    return render(request,'index.html',content)