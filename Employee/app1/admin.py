from django.contrib import admin

# Register your models here.


from django.contrib import admin
from app1.models import Employee

admin.site.register(Employee)