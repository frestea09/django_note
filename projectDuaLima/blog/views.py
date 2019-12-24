from django.shortcuts import render
from . import form
from . import models
# Create your views here.
def index(request):
    objForm = form.Post(request.POST or None)
    content = {
        'judul':'Blog'
    }
    content['form'] = objForm
    if (request.method == 'POST'):
        judulPost = request.POST.get('judul')
        article = request.POST.get('article')
        author = request.POST.get('author')
        content['judulPost'] =judulPost
        content['article'] =article
        content['author'] =author
        if objForm.is_valid():
            models.Post.objects.create(
                judul=objForm.cleaned_data.get('judul'),
                article=objForm.cleaned_data.get('article'),
                author=objForm.cleaned_data.get('author'),
            )
    return render(request,'blog/index.html',content)