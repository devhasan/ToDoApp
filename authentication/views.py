from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegistrationForm
# Create your views here.

# def login(request):
#     return render(request, 'authentication/login.html')

def signup(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            login(request, user)
            return redirect('home')
            #return redirect('login') #To Redirect to login page.

    else:
        form = UserRegistrationForm()
    return render(request, 'authentication/signup.html', {'form': form})