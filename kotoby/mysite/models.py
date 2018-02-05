from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="mysite/static/", null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name()

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
    user = models.ManyToManyField('Profile', blank=True, through="Status")

    def __str__(self):
        return self.title


class Status(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
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
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    rate = models.IntegerField()
    review = models.IntegerField()

    def __str__(self):
        return self.book
