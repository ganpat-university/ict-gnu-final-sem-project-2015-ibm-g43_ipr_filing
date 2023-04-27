from django.db import models

# username = admin
# password = 123

# Create your models here.

class Form1(models.Model):
    A = models.CharField(max_length=512, blank=True)
    B = models.CharField(max_length=512, blank=True)
    type = models.CharField(max_length=512, blank=True)
    C = models.CharField(max_length=512, blank=True)
    D = models.CharField(max_length=512, blank=True)
    Registerd_in_Class = models.CharField(max_length=512, blank=True)
    Under_No = models.CharField(max_length=512, blank=True)
    E1 = models.CharField(max_length=512, blank=True)
    E2 = models.CharField(max_length=512, blank=True)
    E3 = models.CharField(max_length=512, blank=True)
    E4 = models.CharField(max_length=512, blank=True)
    F = models.CharField(max_length=512, blank=True)
    Email = models.CharField(max_length=512, blank=True)
    Mobile = models.CharField(max_length=512, blank=True)
    Declaration = models.CharField(max_length=512, blank=True)
    Day = models.CharField(max_length=2, blank=True)
    Month = models.CharField(max_length=2, blank=True)
    Year = models.CharField(max_length=2, blank=True)
    Sign = models.ImageField(upload_to="Sign/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
