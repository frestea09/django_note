from django.urls import path,re_path
from . import views
app_name = 'blog'
urlpatterns = [
    re_path(r'^$',views.Index.as_view(),name='index'),
    re_path(r'^form/$',views.Create.as_view(),name='create'),
]