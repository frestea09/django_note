from django.urls import path,re_path
from . import views

urlpatterns = [
    re_path(r'^$',views.index,name='index'),
    re_path(r'^(?P<author>[\w-]+)/$',views.authorPost),
    re_path(r'^post/(?P<inputSlug>[\w-]+)/$',views.singlePost),
]