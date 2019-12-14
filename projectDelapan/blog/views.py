from django.shortcuts import render

# Create your views here.

def index(request):
    content = {
        'judulWeb':'Blog',
        'judul':'Blog',
        'article':'Selamat Datang, ini adalah halaman BLog'
    }
    return render(request,'index.html',content)
