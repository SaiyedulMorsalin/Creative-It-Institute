from django.contrib import admin
from .models import AddStudent


# Register your models here.
@admin.register(AddStudent)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["roll", "name", "department"]
