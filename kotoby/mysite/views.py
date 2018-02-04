from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from django.contrib.auth import authenticate,login,logout
# from django.contrib.auth.forms import UserCreationForm

def Home(request):
    if request.user.is_authenticated:
        return render(request, 'mysite/home.html')
    else:
        return redirect('/login')

def redirectToLogin(request):
    if request.user.is_authenticated:
        return redirect('/home', permanent=True)
    else:
        return redirect('/login')

# def Register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('/login')
#     else:
#         form = UserCreationForm()
#         return render(request, 'mysite/register.html',{'form':form})
