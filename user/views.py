from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import CreateUserForm

# Create your views here.

def registrationPage(request):
	if request.user.is_authenticated:
	# if False:
		return redirect('user:home')
	else:
		form = CreateUserForm()

		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				messages.success(request, "Se ha creado la cuenta exitosamente")

				return redirect('user:login')

		context = {'form': form}
		return render(request, 'user/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
	# if False:
		return redirect('user:home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username = username, password = password)

			if user is not None:
				login(request, user)
				redirect('user:home')

			else:
				messages.info(request, 'usuario o contraseña es incorrecto')
				
		context = {}
		return render(request, 'user/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('user:login')

@login_required(login_url='user:login')
def home(request):
	context = {}
	return render(request, 'user/home.html', context)

