from django import forms

class FormBlog(forms.Form):
    title = forms.CharField()
    article = forms.CharField(
        widget=forms.Textarea
    )
    author = forms.CharField()