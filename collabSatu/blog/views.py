from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    content = {
        'sectionWeb':'Blog',
        'sectionWebArticle':'Selamat Datang Blog',
        'titleArticle':'Blog',
        'article':'This Section is blog.',
        'sideMenu':[
            ['/blog/ilman','Ilman'],
            ['/blog/faris','Faris'],
            ['/lies','Lies'],
        ]
    }
    return render(request,'blog/index.html',content)
def ilman(request):
    data = models.Post.objects.filter(author='ilman')
    content = {
        'sectionWeb':'Blog',
        'sectionWebArticle':'Selamat Datang Blog',
        'titleArticle':'Blog Ilman',
        'article':'Berikut adalah article yang ditulis oleh ilman.',
        'sideMenu':[
            ['/blog/ilman','Ilman'],
            ['/blog/faris','Faris'],
            ['/blog/lies','Lies'],
        ],
        'data':data
    }
    return render(request,'blog/index.html',content)
def faris(request):
    data = models.Post.objects.filter(author='faris')
    content = {
        'sectionWeb':'Blog',
        'sectionWebArticle':'Selamat Datang Blog',
        'titleArticle':'Blog Faris',
        'article':'Berikut adalah article yang ditulis oleh Faris.',
        'sideMenu':[
            ['/blog/ilman','Ilman'],
            ['/blog/faris','Faris'],
            ['/blog/lies','Lies'],
        ],
        'data':data
    }
    return render(request,'blog/index.html',content)
def lies(request):
    data = models.Post.objects.filter(author='lies')
    content = {
        'sectionWeb':'Blog',
        'sectionWebArticle':'Selamat Datang Blog',
        'titleArticle':'Blog Lies',
        'article':'Berikut adalah article yang ditulis oleh Lies.',
        'sideMenu':[
            ['/blog/ilman','Ilman'],
            ['/blog/faris','Faris'],
            ['/blog/lies','Lies'],
        ],
        'data':data
    }
    return render(request,'blog/index.html',content)
