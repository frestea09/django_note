from django.views.generic.base import View,TemplateView
from django.shortcuts import render

class Index(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        content = {
            'section':'Home',
            'title':'Home',
            'article':'Selamat Datang, dihome'
        }
        return content