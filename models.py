from django.db import models
from django import forms
# Create your models here.
class Author(models.Model):
    aid = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    born_at = models.DateField(null=True)
    die_at = models.DateField(null=True)
    Bio = models.TextField()

class Books(models.Model):
    bid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    published_at = models.DateField(null=True)
    summary = models.TextField()
    image = models.ImageField(upload_to="projectimg/", null=True, blank=True)
    authors = models.ManyToManyField('Author', blank=True)#book and authors

class Category(models.Model):
    cid = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=50)
    books_cat = models.ManyToManyField('Books', blank=True)#book and category

class User(models.Model):
    uid = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="projectimg/", null=True, blank=True)
    email = models.EmailField()
    password = forms.CharField(max_length=32, widget=forms.PasswordInput)
    book = models.ManyToManyField('Books', blank=True,through='rate_view')

class rate_view(models.Model):#books and user
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerField()
    review = models.IntegerField()
