from django.contrib.auth.models import User
from django import forms
from .models import BlogPost


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'description' ]
        
        
        
class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'image', 'description' ]
