from django.urls import path
from Form_1 import views as v   

urlpatterns=[
    path('',v.form1,name="form1"),

]