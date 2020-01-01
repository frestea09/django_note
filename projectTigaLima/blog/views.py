from django.shortcuts import render,redirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from . import models
from . import form
# Create your views here.
def index(request):
    dataBlog = models.Post.objects.all()
    page = request.GET.get('page',1)
    paginator = Paginator(dataBlog,5)
    try:
        postBlog = paginator.page(page)
    except PageNotAnInteger:
        postBlog = paginator.page(1)
    except EmptyPage:
        postBlog = paginator.page(paginator.num_pages)
    templateName = 'blog/index.html'
    content = {
        'title':'Blog',
        'article':'Selamat Datang diBlog, section ini membahasa mengenai Post pada blog yang telah dibuat',
        'postBlog':postBlog
    }
    return render(request,templateName,content)
def tambah(request):
    objFormBlog = form.FormPost(request.POST or None)
    templateName = 'blog/form.html'
    content = {
        'title':'Form Isi',
        'aritcle':'Tolong isi dengan seksama dan benar',
        'form':objFormBlog,
    }
    if(request.method == 'POST'):
        if (objFormBlog.is_valid()):
            objFormBlog.save()
            return redirect('blog:index')
    return render(request,templateName,content)
def delete(request,inputId):
    models.Post.objects.get(id=inputId).delete()
    return redirect('blog:index')
def update(request,inputId):
    templateName = 'blog/form.html'
    dataPost = models.Post.objects.get(id=inputId)
    data = {
        'author':dataPost.author,
        'article':dataPost.article,
        'title':dataPost.title,
    }
    objForm = form.FormPost(
        request.POST or None,
        initial=data,
        instance= dataPost,
    )
    content = {
        'title':'Update Form',
        'form':objForm
    }
    if(request.method == 'POST'):
        if(objForm.is_valid()):
            objForm.save()
            return redirect('blog:index')
    return render(request,templateName,content)