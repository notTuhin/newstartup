from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = [
			'username', 
			'email', 
			'password1', 
			'password2',
		]

class UserLoginForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'myfieldclass'}))
    password = forms.CharField(label=("Password"), widget=forms.PasswordInput(attrs={'class' : 'mypasswordclass'}))

	
