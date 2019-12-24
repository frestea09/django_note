from django.shortcuts import render

def index(request):
    content = {
        'section':'Home',
        'article':'Selamat data '
    }
    return render(request,'index.html',content)