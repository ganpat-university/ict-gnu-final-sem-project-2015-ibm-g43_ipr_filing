from django.shortcuts import render
from Form_1.models import *
# Create your views here.



def dashboard(request):
    getData = Form1.objects.all()
    return render(request, 'dashboard.html', {"datas":getData})