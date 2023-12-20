from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        max_length=30,
        required=True,
        help_text='' 
     )
    password1 = forms.CharField(
        max_length=30,
        required=True,
        help_text='',
        widget=forms.PasswordInput(),
        label='Password',
        
    ) # Set to False to remove the required validation
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
       