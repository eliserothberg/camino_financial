from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Mobile

admin.site.register(Mobile)

from .models import Student

admin.site.register(Student)