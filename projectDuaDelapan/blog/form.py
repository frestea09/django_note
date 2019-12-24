from django import forms
from . import models
class FormBlog(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = {
            'judul',
            'article',
            'author',
        }
        labels = {
            'judul':'Title',
            'author':'Penulis',
            'article':'Article',
        }
        listPenulis = [
            ['ilman', 'ilman'],
            ['lies','Lies'],
            ['faris','faris'],
            ['deni','Deni'],
        ]

        widgets = {
            'judul': forms.TextInput(
                attrs ={
                    'class':'form-control',
                }
            ),
            'article': forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Tulisan'
                }
            ),
            'author': forms.Select(
                attrs={
                    'class':'form-control',
                },
                choices= listPenulis,
            )
        }