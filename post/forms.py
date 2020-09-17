from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title', 'author', 'publisher', 'pubdate', 'review',)
        dic={
            'review':forms.CharField(widget=forms.Textarea)
        }
