from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView,TemplateView
from django.http import HttpResponse ,HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render_to_response
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .userform import addNewUser
from django.db.models import Avg, Count
from django.db.models import Q
from django import forms
from .models import *


def Home(request):
    if request.user.is_authenticated:
        topRatedBooks_list = User_books.objects.filter(user=request.user.id).annotate(Avg('rate')).filter(rate__gt=3)
        paginator = Paginator(topRatedBooks_list, 2)
        page = request.GET.get('page')
        topRatedBooks = paginator.get_page(page)
        userid = request.user.id
        cat = Category.objects.all()
        request.cat = cat
        return render(request, 'mysite/home.html',{'userid':userid,'topRatedBooks':topRatedBooks})
    else:
        return redirect('/login')

def redirectToLogin(request):
    if request.user.is_authenticated:
        return redirect('/home', permanent=True)
    else:
        return redirect('/login')

def Register(request):
    if request.method=='POST':
        form = addNewUser(request.POST, request.FILES)
        profile = Profile()
        if form.is_valid():
            user = form.save(commit=False)
            if User.objects.filter(username=user):
                form = addNewUser(
                initial={'first_name':request.user.first_name,'last_name':request.user.last_name,'email':request.user.email,'username':request.user.username})
                return render(request, 'mysite/register.html',{'form':form})
            else:
                user.set_password(user.password)
                user.save()
                profile.user = user
                profile.image=form.cleaned_data['image']
                profile.save()
                login(request, user)
                return redirect('/login')
        return render(request, 'mysite/register.html',{'form':form})
    elif request.method=="GET":
        form = addNewUser()
        return render(request, 'mysite/register.html',{'form':form})

def logOut(request):
    if request.method=='GET':
        logout(request)
        return redirect('/login')

def profile(request, pk):
    cat = Category.objects.all()
    request.cat = cat
    if request.method=='GET' and request.user.is_authenticated:
        form = addNewUser(
            initial={'first_name':request.user.first_name,'last_name':request.user.last_name,'email':request.user.email,'username':request.user.username}
        )
        return render(request, 'mysite/profile.html',{'form':form})

    elif request.method=='POST' and request.user.is_authenticated:
        # form = addNewUser(data=request.POST,instance=request.user)
        form = addNewUser(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            if User.objects.filter(username=user) and (user != request.user.username):
                form = addNewUser(
                initial={'first_name':request.user.first_name,'last_name':request.user.last_name,'email':request.user.email,'username':request.user.username})
                return render(request, 'mysite/profile.html',{'form':form})
            else:
                user.set_password(user.password)
                update = User.objects.get(id=pk)
                update.first_name=user.first_name
                update.last_name=user.last_name
                update.email=user.email
                update.username=user.username
                update.password=user.password
                update.save()
                profile.user = user
                profile.image=form.cleaned_data['image']
                updatepic = Profile.objects.get(user_id=request.user.id)
                updatepic.image = profile.image
                updatepic.save()
                return redirect('/login')
        return render(request, 'mysite/profile.html',{'form':form})
    else:
        return redirect('/login')


def authors(request):
    all_authors = Authors.objects.all().order_by('name')
    # authors = Authors.objects.order_by(.asc())
    cat = Category.objects.all()
    request.cat = cat
    paginator = Paginator(all_authors, 2)
    page = request.GET.get('page')
    authors = paginator.get_page(page)
    return render(request, 'mysite/authors.html', {'authors' : authors})

def favorite(request):
    cat = Category.objects.all()
    request.cat = cat
    if request.user.is_authenticated:
        userbooks_list = User_books.objects.filter(Q(user=request.user.id) & Q(status='favourites'))
        paginator = Paginator(userbooks_list, 2)
        page = request.GET.get('page')
        userbooks = paginator.get_page(page)
        return render(request, 'mysite/favorite.html',{'userbooks':userbooks})
    else:
        return redirect('/login')

def now(request):
        cat = Category.objects.all()
        request.cat = cat
        if request.user.is_authenticated:
            userbooks_list = User_books.objects.filter(Q(user=request.user.id) & Q(status='CurrentlyReading'))
            paginator = Paginator(userbooks_list, 2)
            page = request.GET.get('page')
            userbooks = paginator.get_page(page)
            return render(request, 'mysite/currentreading.html',{'userbooks':userbooks})
        else:
            return redirect('/login')

def future(request):
    cat = Category.objects.all()
    request.cat = cat
    if request.user.is_authenticated:
        userbooks_list = User_books.objects.filter(Q(user=request.user.id) & Q(status='FutureReading'))
        paginator = Paginator(userbooks_list, 2)
        page = request.GET.get('page')
        userbooks = paginator.get_page(page)
        return render(request, 'mysite/futurereading.html',{'userbooks':userbooks})
    else:
        return redirect('/login')

def myBooks(request):
    cat = Category.objects.all()
    request.cat = cat
    books = User_books.objects.filter(user=request.user.id)
    rate = [book.rate for book in books]
    status = [book.status for book in books]
    remove = [book.id for book in books]
    books = [b.book for b in books]
    authors = [Books.authors.through.objects.get(books_id = book.id) for book in books]
    authors = [Authors.objects.get(id = a.authors_id) for a in authors]

    for i in range(len(books)):
        book = books[i]
        avg = User_books.objects.filter(book=book.id).aggregate(Avg('rate'))['rate__avg']
        book.author = authors[i].name
        book.author_id = authors[i].id
        book.status = status[i]
        book.remove = remove[i]
        book.rate = rate[i]
        book.avg = avg

    return render(request, 'mysite/mybooks.html', {'books' : books })


def remove(request, remove_id):
    b = User_books.objects.filter(id=remove_id).delete()
    return redirect('mybooks')

def showAuthor(request, author_id):
    cat = Category.objects.all()
    request.cat = cat
    books = Books.authors.through.objects.filter(authors_id=author_id)
    books = [book.books for book in books]
    avgs = [User_books.objects.filter(book=book.id).aggregate(Avg('rate'))['rate__avg'] for book in books]
    author = Authors.objects.get(id=author_id)
    author_name = author.name
    nationality = author.nationality
    born = author.born
    bio = author.Bio
    image = author.image
    return render(request, 'mysite/authorDetails.html',
    {'born' : born,
    'nationality':nationality ,
    'author_name':author_name,
    'bio' : bio,
    'image' : image,
    'author_id' : author_id,
    'books' : books,
    'avgs' : avgs
    })

def showBook(request, book_id):
    cat = Category.objects.all()
    request.cat = cat
    avg = User_books.objects.filter(book=book_id)
    myrating = User_books.objects.filter(book=book_id, user=request.user.id)
    if(myrating):
        myrating = myrating[0].rate
    else:
        myrating = 0
    if(avg):
        avg = avg.aggregate(Avg('rate'))['rate__avg']
    else:
        avg = 0
    book = Books.objects.get(id=book_id)
    author = Books.authors.through.objects.get(id=book_id)
    author = author.authors_id
    author = Authors.objects.get(id=author)
    display_summary = book.summary
    display_authors = book.authors
    author_id = author.id
    title = book.title
    image = book.image
    author_name = author.name
    reviews = User_books.objects.filter(book=book_id)
    users = [ review.user for review in reviews]
    users = [ user.user.first_name + " " + user.user.last_name for user in users]
    for i in range(len(reviews)):
        reviews[i].user_name = users[i]
    return render(request, 'mysite/bookDetails.html', {'display_summary':display_summary,
    'title':title,
    'author_name':author_name,
    'author_id':author_id,
    'image' : image,
    'avg' : avg,
    'myrating' : myrating,
    'id' : book_id,
    'reviews' : reviews
    })

def rate(request):
    r = request.GET.get('rate', None)
    book_id = request.GET.get('book', None)
    exist = User_books.objects.filter(book=book_id, user=request.user.id)
    if(exist):
        User_books.objects.filter(book=book_id, user=request.user.id).update(rate=r)
    else:
        b = Books.objects.get(id=book_id)
        f = Profile.objects.get(id=request.user.id)
        p = User_books(book=b, user=f, status="", rate=r, review=0)
        p.save()

    data = {}
    return JsonResponse(data)

def browse(request, catno):
    cat = Category.objects.all()
    request.cat = cat
    listCat = []
    if(catno == 0):
        cats = Category.objects.all()
        for cat in cats:
            genre = cat.name
            books = Category.book.through.objects.filter(category_id=cat.id)
            books = [Books.objects.get(id=book.books_id) for book in books]
            listCat.append({'genre' : genre, 'books' : books})
    else:
        genre = Category.objects.get(id=catno)
        genre = genre.name
        books = Category.book.through.objects.filter(category_id=catno)
        books = [Books.objects.get(id=book.books_id) for book in books]
        listCat.append({'genre' : genre, 'books' : books})

    return render(request, 'mysite/browse.html', {'listCat' : listCat})

def addBook(request, add_id, state):
    exist = User_books.objects.filter(book=add_id, user=request.user.id)
    if(exist):
        User_books.objects.filter(book=add_id, user=request.user.id).update(status=state)
    else:
        b = Books.objects.get(id=add_id)
        dd = Profile.objects.get(user_id=request.user.id).id
        f = Profile.objects.get(id=dd)
        p = User_books(book=b, user=f, status=state, rate=0, review=" ")
        p.save()
    return redirect(request.META['HTTP_REFERER'])

def search(request):
    cat = Category.objects.all()
    request.cat = cat
    if request.method=='GET':
        searchText = request.GET.get("search")
        books = Books.objects.filter(title__icontains=searchText)
        authors = Authors.objects.filter(name__icontains=searchText)
        return render(request, 'mysite/search.html',{'books':books,'authors':authors})

def review(request):
    rev = request.GET.get('review', None)
    book_id = request.GET.get('book', None)
    exist = User_books.objects.filter(book=book_id, user=request.user.id)
    if(exist):
        User_books.objects.filter(book=book_id, user=request.user.id).update(review=rev)
    else:
        b = Books.objects.get(id=book_id)
        f = Profile.objects.get(user_id=request.user.id)
        p = User_books(book=b, user=f, status="", rate=0, review=rev)
        p.save()

    data = {}
    return JsonResponse(data)
