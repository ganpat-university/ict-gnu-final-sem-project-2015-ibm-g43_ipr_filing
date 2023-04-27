from django.shortcuts import render
from .models import Form3

# Create your views here.
def form3(request):
    if request.method=="POST":
        obj = Form3()
        obj.A = request.POST['A']
        obj.B = request.POST['B']
        obj.service = request.POST['service']
        obj.Day = request.POST['day']
        obj.Month = request.POST['month']
        obj.Year = request.POST['year']
        obj.Sign = request.FILES['sign']
        obj.To = request.POST['to']
        obj.save()
    return render(request,"form3.html")
