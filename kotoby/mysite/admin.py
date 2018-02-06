from django.contrib import admin
from mysite import models

admin.site.register(models.Profile)
admin.site.register(models.Authors)
admin.site.register(models.Books)
<<<<<<< HEAD
# admin.site.register(models.User_books)
=======
admin.site.register(models.User_books)
>>>>>>> 6a378b80aac19c132cb11ab1a5d9847088c95c45
admin.site.register(models.Category)
