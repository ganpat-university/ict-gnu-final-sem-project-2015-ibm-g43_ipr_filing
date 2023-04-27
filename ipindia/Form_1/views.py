from django.shortcuts import render
from .models import Form1
from .form import Form

# Create your views here.

def form1(request):
    if request.method=="POST":
        obj=Form1()
        obj.A=request.POST['A']
        obj.B=request.POST['B']
        obj.C=request.POST['C']
        obj.D=request.POST['D']
        obj.Registerd_in_Class=request.POST['Registerd_in_Class']
        obj.Under_No=request.POST['Under_No']
        obj.E1=request.POST['E1']
        obj.E2=request.POST['E2']
        obj.E3=request.POST['E3']
        obj.E4=request.POST['E4']
        obj.Email=request.POST['Email']
        obj.Mobile=request.POST['Mobile']
        obj.Day=request.POST['Day']
        obj.Month=request.POST['Month']
        obj.Sign=request.FILES['Sign']
        obj.save()
    
    return render(request,"form1.html")


def form1_show(request):
    return render(request, '')


