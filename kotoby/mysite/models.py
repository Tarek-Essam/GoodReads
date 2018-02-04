from django.db import models
from django.contrib.auth.models import User

class Users(User):
    image = models.ImageField(upload_to="imgs/", null=True, blank=True)
    # class meta:
    #     db_table = "users"


class Authors(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    born_at = models.DateField(null=True)
    die_at = models.DateField(null=True)
    Bio = models.TextField()
    # class meta:
    #     db_table = "authors"

class Books(models.Model):
    title = models.CharField(max_length=50)
    published_at = models.DateField(null=True)
    summary = models.TextField()
    image = models.ImageField(upload_to="imgs/", null=True, blank=True)
    authors = models.ManyToManyField('Authors', blank=True)#book and authors
    user = models.ManyToManyField('Users', blank=True, through="Status")
    # class meta:
    #     db_table = "books"

class Status(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = models.CharField(max_length=200)
    # class meta:
    #     db_table = "status"


class Category(models.Model):
    cat_name = models.CharField(max_length=50)
    books_cat = models.ManyToManyField('Books', blank=True)#book and category
    # class meta:
    #     db_table = "category"


class Rate(models.Model):#books and user
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    rate = models.IntegerField()
    review = models.IntegerField()
    # class meta:
    #     db_table = "rate"
