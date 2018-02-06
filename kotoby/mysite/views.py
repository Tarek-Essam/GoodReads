from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from django.contrib.auth import authenticate,login,logout
from .models import *
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

def myBooks(request):
    #books = list(models.Books.objects.values())
    # books = models.Books.objects.select_related('authors')
    # books = books.query
    books = Status.objects.filter(user=2)
    books = [b.book for b in books]
    author
    # books = books.book
    return HttpResponse(books)
    # for book in books:
    #     image = book['image'].split("/")[-1]
    #     book['image'] = image
    # b = {'books' : books}
    # return render(request, 'mysite/mybooks.html', b)
