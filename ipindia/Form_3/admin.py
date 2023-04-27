from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Form3)
class FormAdmin(admin.ModelAdmin):
    list_display = ['id', 'A', 'B', 'service', 'Day', 'Month', 'Year', 'created_at', 'updated_at']