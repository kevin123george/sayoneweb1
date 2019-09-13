from django import forms
from .models import Comment,Post
from django.contrib.auth.models import User

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your Name"
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={
            "class": "form-control",
            "placeholder": "Leave a comment!"
        })
    )


    

class AskForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','body','aut']
    

