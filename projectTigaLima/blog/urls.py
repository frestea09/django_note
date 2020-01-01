from django.urls import path,re_path
from . import views
app_name = 'blog'
urlpatterns = [
    re_path(r'^$',views.index,name='index'),
    re_path(r'^tambah/form/$',views.tambah,name='form'),
    re_path(r'^delete/(?P<inputId>[0-9]+)/$',views.delete,name='delete'),
    re_path(r'^update/(?P<inputId>[0-9]+)/$',views.update,name='update'),
]