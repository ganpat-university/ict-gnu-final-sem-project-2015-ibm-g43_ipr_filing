from django.db import models

# Create your models here.
class Form15(models.Model):
    A = models.CharField(max_length=512, blank=True)
    B = models.CharField(max_length=512, blank=True)
    Furnish_request = models.CharField(max_length=512, blank=True)
    C = models.CharField(max_length=512, blank=True)
    Certificate_To = models.CharField(max_length=2, blank=True)
    Follows = models.CharField(max_length=2, blank=True)
    Day = models.CharField(max_length=2, blank=True)
    Month = models.CharField(max_length=2, blank=True)
    Year = models.CharField(max_length=2, blank=True)
    Sign = models.ImageField(upload_to="Sign/", blank=True)
    To = models.CharField(max_length=2, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)