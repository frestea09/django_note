from django.urls import re_path,path
from django.views.generic import ListView
from . import models
from . import views
app_name = 'blog'
urlpatterns = [
    re_path(r'^$', views.ListView.as_view(),name='index'),
    # re_path(r'^form/',views.Create.as_view(),name='tambah'),
]