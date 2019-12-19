from django.shortcuts import render

# Create your views here.
def index(request):
    content = {
        'judul':'Blog',
        'article':'Welcome to Blog',
        'menu':[
            ['/','Home'],
            ['blog/','Blog'],
        ],
        'menuBlog': [
            ['ilman/', 'ilman'],
            ['blog/', 'Blog'],
        ],
    }
    return render(request,'index.html',content)


def ilman(request):
    content = {
        'judul':'Ilman',
        'article':'Welcome to Ilman',
        'menuBlog':[
            ['blog/ilman','ilman'],
            ['blog/','Blog'],
        ],
    }
    return render(request,'index.html',content)