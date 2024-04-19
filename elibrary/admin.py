from django.contrib import admin
from .models import *

# Register your models here.

# we register models in django admin to manually upload/update their fields
admin.site.register(Books)
admin.site.register(Genere)
admin.site.register(FileType)
admin.site.register(ElibraryUser)
admin.site.register(BookReview)


admin.site.site_header = 'Hezekiah E-library'
admin.site.site_title = 'Hezekiah E-library'
admin.site.site_index_title = 'Welcome to Hezekiah E-library, OAU'