from django.shortcuts import render
from .models import *
# Create your views here.
def getDs(request):
    ds=disease.objects.all()
    return render(request,'diseases.html',{'ds':ds})