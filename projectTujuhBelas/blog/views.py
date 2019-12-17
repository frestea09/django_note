from django.shortcuts import render
from .models import Post
from . import models
# Create your views here.
def index(request):
    isi = models.Post.objects.all()
    content = {
        'judul':'Blog',
        'article':'Hello ini adalah Blog',
        'isi':isi,
    }
    return render(request,'index.html',content)
