from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def loginpage(request):
	page = 'login'

	if request.user.is_authenticated:
		return redirect('home')
		
	if request.method == 'POST':
		username = request.POST.get('username').lower()
		password = request.POST.get('password')

		try:
			user = User.objects.get(username=username)
		except:
			print('User does not exist')	

		tenant = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')	
		else:
			print('Username or password does not exist')		
	context = {'page':page}
	return render(request, 'login_register.html', context)


def registerpage(request):
	form = UserCreationForm()

	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.username = user.username
			user.save()
			login(request, user)
			return redirect('home')
		else:
			print('user not available')
	context = {'form':form}
	return render(request, 'login_register.html', context)

def logoutPage(request):
	logout(request)
	return redirect('login')
