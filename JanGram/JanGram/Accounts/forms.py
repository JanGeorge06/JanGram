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
    email = forms.EmailField(required=True, help_text='Enter a valid email address.')
    date_of_birth = forms.DateField(required=True, help_text='Enter your date of birth (YYYY-MM-DD)')
    profile_photo = forms.ImageField(required=False, help_text='Upload a profile photo (optional)')

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2','email','date_of_birth','profile_photo']
       