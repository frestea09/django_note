from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import models
from . import forms
# Create your views here.
def index(request):
    data = models.Post.objects.all()
    content={
        'sectionWeb':'Blog',
        'judul':'Blog',
        'article':'Selamat Datang di Blog, berikut ada beberapa karya author kami',
        'data':data,
    }
    return render(request,'blog/index.html',content)
def getAuthor(request,slugInput):
    data = models.Post.objects.filter(author=slugInput)
    content = {
        'sectionWeb': 'Blog',
        'judul': 'Blog',
        'article': 'Selamat Datang di Blog, berikut ada beberapa karya author kami',
    }
    content['data'] = data
    return render(request,'blog/index.html',content)
def getDetail(request,slugInput):
    data = models.Post.objects.get(slug=slugInput)
    content = {}
    content['data'] = data
    return render(request,'blog/detail.html',content)
def formTambah(request):
    form = forms.FormBlog()
    content = {
        'sectionWeb': 'Blog',
        'judul': 'Blog',
        'article': 'Selamat Datang di Blog, berikut ada beberapa karya author kami',
    }
    content['form'] = form
    if (request.method == 'POST'):
        models.Post.objects.create(
            title=request.POST['title'],
            article=request.POST['article'],
            author=request.POST['author'],
        )
    return render(request,'blog/form.html',content)
def tambah(request):
    if(request.method=='POST'):
        models.Post.objects.create(
            title=request.POST['title'],
            article = request.POST['article'],
            author = request.POST['author'],
        )
        return HttpResponseRedirect('/blog/')