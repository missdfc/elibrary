from django.contrib import admin
from .models import Books

# Register your models here.

# we register model in django admon to manually upload/update their fields
admin.site.register(Books)

