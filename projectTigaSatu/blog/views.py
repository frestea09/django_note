from django.shortcuts import render,redirect
from django.views.generic.base import TemplateView,View,RedirectView
from . import models
from . import form
# Create your views here.
class Index(TemplateView):
    data = models.Blog.objects.all()
    template_name = 'blog/index.html'
    def get_context_data(self, **kwargs):
        content = {
            'section':'Blog',
            'title':'Blog',
            'article':'Selamat Datang diblog, bagian ini menjelaskan mengenai article yang telah ditulis.',
            'data': self.data,
        }
        return content
class Delete(RedirectView):
    pattern_name = 'blog:index'
    def get_redirect_url(self, *args, **kwargs):
        models.Blog.objects.get(id=deleteId).delete()
        return super().get_redirect_url(self, *args, **kwargs)
# class Create(TemplateView):
#     template_name = 'blog/form.html'
#     form = None
#     mode = None
#     content = {}
#     def get(self,*args,**kwargs):
#         self.form = form.FormBlog()
#         self.content ={
#             'title':'Form',
#             'form':self.form,
#         }
#         return render(self.request,self.template_name,self.content)