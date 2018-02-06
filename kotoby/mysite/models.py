from django.db import models
from django.contrib.auth.models import User

class Users(User):
    image = models.ImageField(upload_to="mysite/static/", null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

    def get_image(self):
        image = self.image
        image = split("/")
        image = image[-1]
        return image


class Authors(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    born_at = models.DateField(null=True)
    die_at = models.DateField(null=True)
    Bio = models.TextField()

    def __str__(self):
        return self.first_name + self.last_name



class Books(models.Model):
    title = models.CharField(max_length=50)
    published_at = models.DateField(null=True)
    summary = models.TextField()
    image = models.ImageField(upload_to="mysite/static/", null=True, blank=True)
    authors = models.ManyToManyField('Authors', blank=True)#book and authors
    user = models.ManyToManyField('Users', blank=True, through="Status")

    def get_image(self):
        image = self.image
        image = split("/")
        image = image[-1]
        return image

    def __str__(self):
        return self.title


class Status(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.status


class Category(models.Model):
    name = models.CharField(max_length=50)
    book = models.ManyToManyField('Books', blank=True)#book and category

    def __str__(self):
        return self.name

class Rate(models.Model):#books and user
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    rate = models.IntegerField()
    review = models.IntegerField()

    def __str__(self):
        return self.book
