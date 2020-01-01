from django.urls import re_path,path
from . import views
app_name = 'blog'
urlpatterns = [
    re_path(r'^$',views.Index.as_view(),name='index'),
    re_path(r'^tambah/form',views.Create.as_view(),name='createForm'),
    # \re_path(r'^delete/(?P<deleteId>[0-9]+)/$',views.Delete.as_view(),name='delete'),
]