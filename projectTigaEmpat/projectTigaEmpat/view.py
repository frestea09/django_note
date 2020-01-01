from django.shortcuts import render,redirect

def index(request):
    templateName = 'index.html'
    content = {
        'title':'Home',
        'article':'Selamat Datang dihome, ini adalah latihan website menggunakan django'
    }
    return render(request,templateName,content)