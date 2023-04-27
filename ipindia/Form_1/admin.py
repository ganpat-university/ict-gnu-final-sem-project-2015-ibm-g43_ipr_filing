from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Form1)
class FormAdmin(admin.ModelAdmin):
    list_display = ['id', 'A', 'B', 'type', 'C', 'D', 'Registerd_in_Class', 'Under_No', 'E1', 'E2', 'E3', 'E4', 'F', 'Email', 'Mobile', 'Declaration', 'created_at', 'updated_at']
