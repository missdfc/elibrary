from django.contrib import admin
from .models import *
#Genere, FileType

# Register your models here.

# we register models in django admin to manually upload/update their fields
admin.site.register(Books)
admin.site.register(Genere)
admin.site.register(FileType)
admin.site.register(ElibraryUser)
admin.site.register(BookReview)

