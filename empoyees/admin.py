from django.contrib import admin
from .models import *

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(Employees, EmployeesAdmin)