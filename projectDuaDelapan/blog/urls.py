from django.urls import path,re_path
from . import views
app_name = 'blog'
urlpatterns = [
    re_path(r'^$',views.index,name='index'),
    re_path(r'^tambah/form/$',views.formTambah,name='formTambah'),
    re_path(r'^tambah/create/$',views.create,name='create'),
    re_path(r'^form/delete/(?P<var>[0-9]+)/$',views.delete,name='delete'),
    re_path(r'^form/update/(?P<var>[0-9]+)/$',views.update,name='update'),
]