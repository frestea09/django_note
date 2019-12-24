from django.shortcuts import render
from . import models
# Create your views here.
def index(request):
    data = models.Post.objects.all()
    content = {
        'sectionWeb':'Blog',
        'sectionWebDesc':'Section ini mengenai Blog Website',
        'sectionWebDescDetail':'Website ini mengenai pelatihan ilman menggunakan django. Data yangdipergunakan adalah data blog.',
        'nav':[
            ['/','all'],
            ['ilman/','ilman'],
            ['faris/','faris'],
            ['lies/','lies'],
         ],
        'data': data,
    }
    return render(request,'blog/index.html',content)

def getReadDetail(request,slugInput):
    data = models.Post.objects.get(slug=slugInput)
    content = {
        'sectionWeb':'Blog',
        'sectionWebDesc':'Section ini mengenai Blog Website',
        'sectionWebDescDetail':'Website ini mengenai pelatihan ilman menggunakan django. Data yangdipergunakan adalah data blog.',
        'nav':[
            ['/','all'],
            ['ilman/','ilman'],
            ['faris/','faris'],
            ['lies/','lies'],
         ],
        'data': data,
    }
    return render(request,'blog/detail.html',content)
def getByAuthor(request,input):
    data = models.Post.objects.filter(author=input)
    content = {
        'sectionWeb':'Blog',
        'sectionWebDesc':'Section ini mengenai Blog Website',
        'sectionWebDescDetail':'Website ini mengenai pelatihan ilman menggunakan django. Data yangdipergunakan adalah data blog.',
        'nav':[
            ['/blog/','all'],
            ['/blog/ilman/','ilman'],
            ['/blog/faris/','faris'],
            ['/blog/lies/','lies'],
         ],
        'data': data,
    }
    return render(request,'blog/index.html',content)
