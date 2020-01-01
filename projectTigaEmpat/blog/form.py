from django import forms
from . import models
class FormPost(forms.ModelForm):
    class Meta:
        model = models.Post
        labels = {
            'title': 'Judul',
            'auhtor': 'Penulis',
            'article': 'Karya Tulis',
        }
        fields = {
            'title',
            'author',
            'article',
        }