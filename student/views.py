from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request,'student/register.html')

def homepage(request):
    return render(request,'/student/home.html')

def login(request):
    return render(request,'student/login.html')