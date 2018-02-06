from django.contrib import admin
from mysite import models

admin.site.register(models.Profile)
admin.site.register(models.Authors)
admin.site.register(models.Books)
# admin.site.register(models.User_books)
admin.site.register(models.Category)
