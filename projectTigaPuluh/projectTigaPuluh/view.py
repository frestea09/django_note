from django.shortcuts import render
from django.views.generic.base import TemplateView,View,RedirectView
class Home(RedirectView):
    pattern_name = 'index'
class Index(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        content = {
            'title':'Home',
            'article':'Selamat Datang di home'
        }
        return content
class Name(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        content = {}
        content['title'] = 'Author'
        content['article'] = 'ini adalah section mengnai article'
        content = kwargs
        return content
class Ilman(View):
    template_name = 'index.html'
    content = {
        'title':'Ilman'
    }
    def get(self,request):
        return render(request,self.template_name,self.content)
    def post(self,request):
        self.content['data'] = request.POST.get('name')
        return render(request,self.template_name,self.content)
class About(TemplateView):
    pass