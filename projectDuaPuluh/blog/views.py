from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    content = {}
    data = models.Post.objects.filter(author='ilman')
    content['data'] = data
    return  render(request,'blog/index.html',content)
def faris(request):
    content = {}
    data = models.Post.objects.filter(author='faris')
    content['data'] = data
    return  render(request,'blog/index.html',content)