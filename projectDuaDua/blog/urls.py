from django.urls import path,re_path
from . import views
app_name = 'blog'
urlpatterns = [
    re_path(r'^$',views.index,name='index'),
    re_path(r'^(?P<input>[\w]+)/$',views.getByAuthor,name='author'),
    re_path(r'^post/(?P<slugInput>[\w-]+)/$',views.getReadDetail,name='detail'),
]