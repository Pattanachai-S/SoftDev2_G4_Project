from django.http.response import HttpResponse
from django.shortcuts import render



def home(request):
    return render(request, 'generalApp/home.html')

def about_us(request):
    return render(request, 'generalApp/aboutus.html')