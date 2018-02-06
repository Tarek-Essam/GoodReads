from django.contrib import admin
from mysite import models

admin.site.register(models.Users)
admin.site.register(models.Authors)
admin.site.register(models.Books)
admin.site.register(models.Status)
admin.site.register(models.Category)
admin.site.register(models.Rate)
