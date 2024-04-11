from .models import Post
from django import forms


class NewsForm(forms.ModelForm):
   class Meta:
       model = Post
       fields = {
           'author': ['exact'],
           'heading':[''],
           'text':[''],
       }