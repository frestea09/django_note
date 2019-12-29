from django import forms
from . import models
class FormBlog(forms.Form):
    class Meta:
        model = models.Post
        fields = {
            'author',
            'article',
            'title',
        }
        labels = {
            'author':'Penulis',
            'article':'Tulisan',
            'title':'Judul'
        }
        widgets = {
            'author':forms.TextInput(
                attrs={
                    'class':'class-form',
                }
            ),
            'article':forms.TextInput(
                attrs={
                    'class':'class-form',
                }
            ),
        },
