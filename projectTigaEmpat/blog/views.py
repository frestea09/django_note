from django.shortcuts import render,redirect
from . import models
from . import form
# Create your views here.
def index(request):
    templateName = 'blog/index.html'
    dataPost = models.Post.objects.all()
    content = {
        'title':'blog',
        'article':'Selamat Data diBlog, pada bagian ini akan menejlaskan mengenai blog',
        'data':dataPost
    }
    return render(request,templateName,content)
def delete(request,deleteId):
    models.Post.objects.get(id=deleteId).delete()
    return redirect('blog:index')
def getFormBlog(request):
    templateName = 'blog/form.html'
    objForm = form.FormPost(request.POST or None)
    dataForm = form.FormPost()
    content = {
        'title':'Form Plog',
        'form': dataForm,
    }
    if (request.method == 'POST'):
        if (objForm.is_valid()):
            objForm.save()
            return redirect('blog:index')
    return  render(request,templateName,content)
def savePost(request):
    objForm = form.FormPost(request.POST or None)
    if(objForm.is_valid()):
        objForm.save()
        return redirect('blog:index')
def getFormUpdate(request,inputId):
    templateName = 'blog/form.html'
    dataPost = models.Post.objects.get(id=inputId)
    data = {
        'author': dataPost.author,
        'article':dataPost.article,
    }
    formPost = form.FormPost(
        request.POST or None,
        initial=data,
        instance=dataPost,
    )
    content = {
        'form':formPost,
    }
    if (request.method == 'POST'):
        if (formPost.is_valid()):
            formPost.save()
            return redirect('blog:index')
    return render(request,templateName,content)
