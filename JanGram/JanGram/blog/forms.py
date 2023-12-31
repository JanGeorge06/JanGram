from django.forms import ModelForm
from .models import Post
from django import forms

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['image','caption']
    caption = forms.CharField(widget=forms.Textarea, required=False)
