from django.contrib import admin
from .models import Tutors,Students
# Register your models here.


class TutorsAdmin(admin.ModelAdmin):
    list_display = ['name', 'cellno', 'email']


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'fathername', 'area', 'cellno', 'email', 'address']