from django.shortcuts import redirect, render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'about.html')

# def about(request):
#     return render(request, 'about.html')

def education(request):   
    return render(request, 'education.html')

def experience(request):   
    return render(request, 'experience.html')