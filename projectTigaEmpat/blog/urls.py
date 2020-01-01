from django.urls import path,re_path
from . import views
app_name = 'blog'
urlpatterns =[
    re_path(r'^$',views.index,name='index'),
    re_path(r'^delete/(?P<deleteId>[0-9]+)/$',views.delete,name='delete'),
    re_path(r'^tambah/',views.getFormBlog,name='formPost'),
    re_path(r'^tambah/save/$',views.savePost,name='savePost'),
    re_path(r'^update/form/(?P<inputId>[0-9]+)',views.getFormUpdate,name='update'),
]