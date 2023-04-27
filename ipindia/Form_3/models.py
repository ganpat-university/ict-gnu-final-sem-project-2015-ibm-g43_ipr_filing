from django.db import models

# Create your models here.
class Form3(models.Model):
    A = models.CharField(max_length=512, blank=True)
    B = models.CharField(max_length=512, blank=True)
    service = models.CharField(max_length=512, blank=True)
    Day = models.CharField(max_length=2, blank=True)
    Month = models.CharField(max_length=2, blank=True)
    Year = models.CharField(max_length=2, blank=True)
    Sign = models.ImageField(upload_to="Sign/", blank=True)
    To = models.CharField(max_length=2, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

