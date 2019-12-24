from django.shortcuts import render,redirect
from . import models
from . import form
# Create your views here.
def index(request):
    data = models.Post.objects.all()
    content = {
        'judul':'Blog',
        'data':data,
    }
    return render(request,'blog/index.html',content)
def createPost(request):
    objForm = form.FormBlog(request.POST or None)
    content = {
        'judul':'Blog',
        'formBlog':objForm,
    }
    if(request.method == 'POST'):
        if(objForm.is_valid()):
            objForm.save()
            return redirect('blog:index')
    return render(request,'blog/form.html',content)

def delete(request,inputId):
    models.Post.objects.get(id=inputId).delete()
    return redirect('blog:index')

def update(request,inpuId):
    pass