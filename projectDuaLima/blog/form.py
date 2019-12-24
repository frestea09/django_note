from django import forms

class Post(forms.Form):
    judul = forms.CharField(max_length=50)
    article = forms.CharField(
        widget=forms.Textarea
    )
    author = forms.CharField(max_length=50)
