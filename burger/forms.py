from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import *


class BookingForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("name", "email", "phone", "date", "time", "guest")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ("name", "email", "text")


class RegisterUserForm(UserCreationForm):
    # username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    # email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    # password1 = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    # password2 = forms.CharField(label='password again', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



