from django.shortcuts import render,redirect
from . import form
from . import models
# Create your views here.
def index(request):
    data = models.Post.objects.all()
    content={
        'section':'Blog',
        'article':'Selamat Datang diBlog. ',
        'data':data
    }
    return render(request,'blog/index.html',content)
def formTambah(request):
    objForm = form.FormBlog()
    content={
        'section':'Blog',
        'article':'Selamat Datang diBlog. ',
        'form': objForm,
    }
    return render(request,'blog/form.html',content)
def create(request):
    objForm = form.FormBlog(request.POST or None)
    if (request.method == 'POST'):
        if (objForm.is_valid()):
            objForm.save()
            return redirect('blog:index')
def delete(request,var):
    models.Post.objects.get(id=var).delete()
    return redirect('blog:index')
def update(request,var):
    data = models.Post.objects.get(id=var)
    dataPost = {
        'judul':data.judul,
        'article':data.article,
        'author':data.author,
    }
    formData = form.FormBlog(
        request.POST or None,
        initial=dataPost,
        instance=data,

    )
    content = {
        'form':formData,
    }
    if(request.method=='POST'):
        if(formData.is_valid()):
            formData.save()
            return redirect('blog:index')
    return render(request,'blog/form.html',content)

