from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.
def index(request):
    return render(request,'index.html')
def authorPost(request,author):
    data = models.Post.objects.filter(author=author)
    content = {}
    content['data'] =data
    return render(request,'index.html',content)
def singlePost(request,inputSlug):
    data = models.Post.objects.get(slug=inputSlug)
    judul  = '<h1>{}</h1'.format(data.judul)
    return HttpResponse(judul)