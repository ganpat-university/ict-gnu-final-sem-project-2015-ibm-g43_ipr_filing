from django.shortcuts import render
from .models import Form15

# Create your views here.

def form15(request):
    if request.method=='POST':
        obj=Form15()
        obj.A=request.POST['A']
        obj.B=request.POST['B']
        obj.Furnish_request=request.POST['Furnish_request']
        obj.C=request.POST['C']
        obj.Certificate_To=request.POST['Certificate_To']
        obj.Follows=request.POST['Follows']
        obj.Day=request.POST['Day']
        obj.Month=request.POST['Month']
        obj.Year=request.POST['Year']
        obj.Sign=request.FILES['Sign']
        obj.To=request.POST['To']
        obj.save()
    return render(request,"form15.html")
