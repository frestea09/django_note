from django.shortcuts import render

def index(request):
    content = {
        'titleWeb':'Home',
        'judulArticle': 'Home',
        'article':'Selamat Datang Dihome, section ini menjelaskan mengenai pembuatan website yang dibuat menggunkan Django',
        'nav':[
            ['/','Home'],
            ['/blog','Blog'],
            ['/about','About'],
        ]
    }
    return render(request,'index.html',content)