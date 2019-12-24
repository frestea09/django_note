from django.urls import path,re_path
from . import views
app_name = 'blog'
urlpatterns = [
    re_path(r'^$',views.index,name='index'),
    re_path(r'^(?P<slugInput>[\w-]+)/$',views.getAuthor,name='detailAuthor'),
    re_path(r'^post/(?P<slugInput>[\w-]+)/$',views.getDetail,name='detailArticle'),
    re_path(r'^tambah/formTambah/$',views.formTambah,name='form'),
    re_path(r'^tambah/formTambah/$',views.tambah,name='tambah'),
]