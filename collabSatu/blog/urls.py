from django.urls import re_path,path
from . import views
urlpatterns = [
    re_path(r'^$',views.index),
    re_path(r'^ilman/$',views.ilman),
    re_path(r'^faris/$',views.faris),
    re_path(r'^lies/$',views.lies),
]