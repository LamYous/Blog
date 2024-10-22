from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, LoginForm, UserUpdateForm, ProfileUpdateForm

from django.contrib.auth import authenticate, login, logout

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegisterForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/register.html', context)

def log_in(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()

    context = {
        'form':form
    }
    return render(request, 'accounts/login.html', context)

def log_out(request):
    logout(request)
    return redirect('login')

def profile(request):

    user = request.user

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST or None, instance=user)
        p_form = ProfileUpdateForm(request.POST or None, request.FILES or None, instance=user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm( instance=user)
        p_form = ProfileUpdateForm(instance=user.profile)
    context = {
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request, 'accounts/profile.html', context)

