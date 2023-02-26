from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from .forms import EtudiantForm,LoginForm
from .models import Etudiant
# Create your views here.

"""def login_view(request):

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            clean=form.cleaned_data
            etudiant=Etudiant.objects.filter(email=clean["email"],password=clean["password"])

            if etudiant.exists():
                name="welcome "+ etudiant[0].prenom +" "+etudiant[0].nom+ " to our home page"
                return render(request,"student/home.html",{"name":name})

            else:
                return render(request,"student/home.html",{"name":"T'es pas inscris!!!"})
        
    else:
        print("Didn't Work")
        form = LoginForm()

    return render(request,"student/login.html",{"form":LoginForm(),"hey":""})
"""


def login_view(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            

            etudiant = authenticate(request, username=username, password=password)
            
            if etudiant is not None:
                login(request, etudiant)
                return render(request, 'student/home.html', {'name': 'hey'})
            
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
            new_student.save()
            print("Worked")
            return render(request,'student/register.html',{
                'form': EtudiantForm(),
                'success':True
            })
    else:
        print("Didint Work")
        form = EtudiantForm()
    return render(request, 'student/register.html',{
        'form': EtudiantForm()
    })


def homepage(request):
    return render(request,'/student/home.html')

