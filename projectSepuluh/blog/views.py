from django.shortcuts import render

# Create your views here.
def index(request):
    content = {
        'judul':'Blog',
        'article':'Selamat Data di blog.',
        'menu':[
            ['/','Home'],
        ],
    }
    return render(request,'index.html',content)
