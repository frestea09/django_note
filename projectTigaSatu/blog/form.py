from django import forms
from . import models

class FormBlog(forms.ModelForm):
    class Meta:
        model = models.Blog
        fields = {
            'author',
            'title',
            'article',
        }