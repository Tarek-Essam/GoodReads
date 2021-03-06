from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="users", null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()

class Authors(models.Model):
    name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    born = models.CharField(max_length=100)
    Bio = models.TextField()
    image = models.ImageField(upload_to="authors", null=True, blank=True)
    def __str__(self):
        return self.name



class Books(models.Model):
    title = models.CharField(max_length=50)
    published_at = models.DateField(null=True)
    summary = models.TextField()
    image = models.ImageField(upload_to="books", null=True, blank=True)
    authors = models.ManyToManyField('Authors', blank=True)#book and authors
    user = models.ManyToManyField('Profile', blank=True, through="User_books")

    def __str__(self):
        return self.title


class User_books(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status = models.CharField(max_length=200)
    rate = models.IntegerField()
    review = models.TextField()

    def __str__(self):
        return self.status


class Category(models.Model):
    name = models.CharField(max_length=50)
    book = models.ManyToManyField('Books', blank=True)#book and category

    def __str__(self):
        return self.name
