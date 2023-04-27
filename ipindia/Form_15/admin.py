from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Form15)
class FormAdmin(admin.ModelAdmin):
    list_display = ['id', 'A', 'B', 'Furnish_request', 'C', 'Certificate_To', 'Follows', 'Day', 'Month', 'Year', 'To', 'created_at', 'updated_at']