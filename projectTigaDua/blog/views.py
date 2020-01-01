from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView,View,RedirectView
from . import form
from . import models
# Create your views here.

class Index(TemplateView):
    template_name = 'blog/index.html'
    data = models.Post.objects.all()
    def get_context_data(self, **kwargs):
        content={
            'title':'Blog',
            'article':'Selamat Datang di blog',
            'dataBlog': self.data,
        }
        return content

class Create(TemplateView):
    template_name = 'blog/form.html'
    form = None
    content = {}
    def get(self, *args, **kwargs):
        self.form = form.FormPost()
        self.content = {
            'title':'Isi Form',
            'form':self.form
        }
        return render(self.request,self.template_name,self.content)
    def post(self,*args,**kwargs):
        self.form = form.FormPost(self.request.POST or None)
        if(self.form.is_valid()):
            if(self.request.method == 'POST'):
                self.form.save()
                return redirect('blog:index')
#
# class Delete(RedirectView):
#     pattern_name = 'blog:index'
#     def get_redirect_url(self, *args, **kwargs):
#         deleteId = kwargs['deleteId']
#         models.Post.objects.filter(id=deleteId).delete()
#         return super().get_redirect_url()
