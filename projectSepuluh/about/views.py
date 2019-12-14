from django.shortcuts import render

# Create your views here.
def index(request):
    content = {
        'judul':'about',
        'article':'Selamat Data di about',
        'menu':[
            ['/','Home'],
        ],
    }
    return render(request,'index.html',content)

