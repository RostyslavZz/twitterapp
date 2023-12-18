from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Comment

class Registration(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {'username': forms.TextInput(attrs={'class' : 'rglines'}),
                   'email' : forms.EmailInput(attrs={'class' : 'rglines'}),
                   'password1' : forms.PasswordInput(attrs={'class' : 'rglines'}),
                   'password2' : forms.PasswordInput(attrs={'class': 'rglines'})
                   }


class Login(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {'username': forms.TextInput(attrs={'class': 'rglines'}),
                   'password': forms.PasswordInput(attrs={'class': 'rglines'})}

class Comments(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {'text': forms.TextInput(attrs={'class': 'postfield', 'placeholder' : 'Comment'})}