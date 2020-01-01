from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView,View,RedirectView
from django.views.generic import ListView
from . import models
from . import form
# Create your views here.
class PostIndex(ListView):
    model = models.Post
    ordering = ['title']
class Index(TemplateView):
    template_name = 'blog/index.html'
    dataPost = models.Post.objects.all()
    content = {}
    def get_context_data(self,*args, **kwargs):
        self.content = {
            'title':'Blog',
            'article':'Belajar Blog',
            'data':self.dataPost,
        }
        return self.content
class FormTambah(TemplateView):
    template_name = 'blog/form.html'
    formBlog = form.FormBlog
    content = {}
    def get_context_data(self,*args, **kwargs):
        self.content = {
            'title':'Blog',
            'article':'Belajar Blog',
            'form':self.formBlog
        }
        return self.content
class Create(View):
    template_name = 'blog/form.html'
    formBlog = form.FormBlog
    form = None
    def get(self,request):
        content = {
            'title':'Blog',
            'article':'Belajar Blog',
            'form':self.formBlog
        }
        return render(request,self.template_name,content)
    def post(self,request):
        self.form = form.FormBlog(self.request.POST or None)
        if (self.form.is_valid()):
            self.form.save()
            return redirect('blog:index')
def index(request):
    template_name = 'blog/index.html'
    dataPost = models.Post.objects.all()
    content = {
        'title': 'Blog',
        'article': 'Belajar Blog',
        'data': dataPost,
    }
    return render(request,template_name,content)