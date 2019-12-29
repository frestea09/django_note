from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

class TemplateIndex(TemplateView):
    pass
class IndexClass(View):
    templateName = 'index.html'
    content = {
        'judul':'hello word'
    }
    def get(self,request):
        return render(request,self.templateName,self.content)
    def post(self,request):
        self.content['data'] = request.POST.get('name')
        return render(request,self.templateName,self.content)
class viewContent(TemplateView):
    template_name = 'content.html'
    def get_context_data(self, **kwargs):
        content = {
            'judul':'Home',
            'author':'ilman',
        }
        return content
class ParameterView(TemplateView):
    template_name = 'parameter.html'
    def get_context_data(self,*args, **kwargs):
        content = {}
        content['judul'] = 'Home'
        content['author'] = 'ilman'
        content = kwargs
        return content

