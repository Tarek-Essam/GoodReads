from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from django.contrib.auth import authenticate,login,logout
from .userform import addNewUser
from django.contrib.auth.models import User


def Home(request):
    if request.user.is_authenticated:
        fname = request.user.first_name
        return render(request, 'mysite/home.html')
    else:
        return redirect('/login')

def redirectToLogin(request):
    if request.user.is_authenticated:
        return redirect('/home', permanent=True)
    else:
        return redirect('/login')

def Register(request):
    if request.method=='POST':
        form = addNewUser(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            form.save()
            login(request, user)
            return redirect('/login')
    else:
        form = addNewUser()
        return render(request, 'mysite/register.html',{'form':form})

def logOut(request):
    if request.method=='GET':
        logout(request)
        return redirect('/login')

# @login_required(login_url='/login')
def Profile(request, pk):
    if request.method=='GET' and request.user.is_authenticated:
        form = addNewUser(
            initial={'first_name':request.user.first_name,'last_name':request.user.last_name,'email':request.user.email,'username':request.user.username}
        )
        return render(request, 'mysite/profile.html',{'form':form})
    elif request.method=='POST' and request.user.is_authenticated:
        form = addNewUser(data=request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            user.save()
            login(request, user)
            return redirect('/login')
    else:
        return redirect('/login')

# def mybooks(request):
    # return render(request, 'mysite/mybooks.html')

def authors(request):
    return render(request, 'mysite/authors.html')

def favorite(request):
    return render(request, 'mysite/favorite.html')

def now(request):
    return render(request, 'mysite/currentreading.html')

def future(request):
    return render(request, 'mysite/futurereading.html')

def myBooks(request):
    #books = list(models.Books.objects.values())
    # books = models.Books.objects.select_related('authors')
    # books = books.query
    books = Status.objects.filter(user=2)
    books = [b.book for b in books]
    # author
    # books = books.book
    return HttpResponse(books)
    # for book in books:
    #     image = book['image'].split("/")[-1]
    #     book['image'] = image
    # b = {'books' : books}
    # return render(request, 'mysite/mybooks.html', b)
