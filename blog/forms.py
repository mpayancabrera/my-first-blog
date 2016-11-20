from django import forms

from .models import Post

from django.contrib.auth.models import User

from django.forms import ModelForm

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'img')

class SignUpForm(ModelForm):
    
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput(),
        }

class LoginForm(ModelForm):
    
    class Meta:
        model = User
        fields = ('username', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }