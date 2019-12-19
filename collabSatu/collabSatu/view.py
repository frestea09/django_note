from django.shortcuts import render

def index(request):
    content = {
        'sectionWeb':'Home',
        'sectionWebArticle':'Selamat Datang dihome.',
    }
    return render(request,'index.html',content)