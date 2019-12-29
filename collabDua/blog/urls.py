from django.urls import path, re_path
from . import views
app_name='blog'
urlpatterns = [
    re_path(r'^$',views.Index.as_view(template_name='snippets/landing_page.html'),name='index')
]