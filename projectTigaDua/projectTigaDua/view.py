from django.views.generic.base import TemplateView,RedirectView,View

class Index(TemplateView):
    template_name = 'index.html'
    def get_context_data(self,**kwargs):
        content={
            'title':'Home',
            'article':'Selamat Datang, ini adalah home',
        }
        return content