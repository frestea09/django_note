from django import forms
from . import models
class FormPost(forms.ModelForm):
    class Meta:
        model = models.Post
        labels = {
            'title':'Judul',
            'author':'Penulis',
            'article':'Artikel',
        }
        fields = {
            'title',
            'article',
            'author',
        }