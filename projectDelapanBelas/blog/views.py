from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    data = models.Post.objects.all()
    content = {
        'judul':'Blog',
        'article': 'Selamat Datang diBlog.',
        'data':data,
    }
    return render(request,'blog/index.html',content)