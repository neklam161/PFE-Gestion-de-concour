from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import EtudiantForm,LoginForm
from .models import Etudiant
from django.contrib.auth.models import User



def login_view(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            

            etudiant = authenticate(request, username=username, password=password)
            
            if etudiant is not None:
                login(request, etudiant)
                return render(request, 'student/index.html', {'name': 'hey'})
            
            else:
                return render(request, 'student/login.html', {'form':LoginForm(),'error': 'Invalid email or password.'})
            
    else:
        form = LoginForm()
    return render(request, 'student/login.html', {'form': LoginForm(),'error':''})

def logout_view(request):
    logout(request)
    return redirect('login')



def register(request):
    if request.method == 'POST':
        form = EtudiantForm(request.POST)
        if form.is_valid():
        
            new_cne = form.cleaned_data["cne"]
            new_nom = form.cleaned_data["nom"]
            new_prenom = form.cleaned_data["prenom" ]
            new_email = form.cleaned_data["email" ]
            new_password= form.cleaned_data["password"]
            new_confpassword= form.cleaned_data["confirmpassword"]
            new_DateNaissance = form.cleaned_data["DateNaissance"]
            new_Numerotelephone = form.cleaned_data["Numerotelephone"]

            new_student = Etudiant(
               cne = new_cne,
               nom = new_nom,
               prenom = new_prenom,
               email = new_email,
               password = new_password,
               confirmpassword = new_confpassword,
               DateNaissance = new_DateNaissance,
               Numerotelephone = new_Numerotelephone
               )
            new_user= User(
                username=new_nom,
                password=new_password,
                email=new_email,
                is_staff=0,
                is_superuser=1
            )
            new_student.save()
            new_user.save()
            messages.success(request, 'Votre compte a été créé avec succès. Veuillez vous connecter pour accéder à votre compte.')
            return redirect('login')
    else:
        form = EtudiantForm()
    return render(request, 'student/register.html',{
        'form': EtudiantForm()
    })


def homepage(request):
    return render(request,'student/index.html')

def concour(request):
    return render(request,'student/concour.html')