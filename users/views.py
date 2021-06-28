from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import views as auth_views
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required



# Create your views here.

def signupPageview(request, *args, **kwargs):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST or None)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			messages.success(request, f'account has been created for {username}! successfully')
			return redirect('login')

	else:
		form = UserRegistrationForm()

	context = {
		'userform': form
	}
	return render(request, 'signup.html', context)
