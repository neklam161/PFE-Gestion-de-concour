from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from uni_admin.models import University_admin

@csrf_protect
def login_view(request):

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            

            user = authenticate(request, username=username, password=password)
             
            if user is not None:
                login(request, user)
                print("User '{}' logged in successfully.".format(user.username))

                if hasattr(user, 'etudiant'):
                    return redirect("studentpage")
                elif hasattr(user, 'university_admin'):
                    return redirect("concour")
            
            else:
                return render(request, 'student/login.html', {'form':LoginForm(),'error': 'Invalid email or password.'})
        else:
            print("Form is invalid.")

            
    else:
        print("something is broken")
        form = LoginForm()
    return render(request, 'student/login.html', {'form': form})

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
            hashed_password = make_password(new_password)
            new_user= User(
                username=new_nom,
                password=hashed_password,
                email=new_email,
            )
            new_user.save()
            new_student = Etudiant(
               user=new_user,
               cne = new_cne,
               nom = new_nom,
               prenom = new_prenom,
               email = new_email,
               password = hashed_password,
               confirmpassword = new_confpassword,
               DateNaissance = new_DateNaissance,
               Numerotelephone = new_Numerotelephone
            )
            new_student.save()
            messages.success(request,'Votre compte a été créé avec succès. Veuillez vous connecter pour accéder à votre compte.')
            return redirect('login')
    else:
        form = EtudiantForm()
    return render(request, 'student/register.html',{'form': form})


def homepage(request):
    return render(request,'student/index.html')

@login_required
def concour(request):
    etudiant = request.user.etudiant
    list_concours = concours.objects.all()
    search_term = request.GET.get('q')
    if search_term:
        list_concours = list_concours.filter(name__icontains=search_term)
    return render(request,'student/concour.html',{"list_concours" : list_concours,"etudiant":etudiant})

@login_required
def profile(request):
    etudiant = Etudiant.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=etudiant)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
    else:
        form = ProfileForm(instance=etudiant)
    return render(request, 'student/profile.html', {'etudiant': etudiant, 'form': form})

def inscrire(request,concour_id):


    if request.method == 'POST':
        form = inscri_concour(request.POST)
        if form.is_valid():
        
            new_cne = form.cleaned_data["cne"]
            new_nom = form.cleaned_data["nom"]
            new_prenom = form.cleaned_data["prenom" ]
            new_email = form.cleaned_data["email"]
            new_note = form.cleaned_data["note" ]
            
            new_etudiant = Etudiant.objects.get(cne=new_cne)
            new_concour = concours.objects.get(id = concour_id)

            if new_etudiant:
                new_inscription = attente(
                    etudiant = new_etudiant,
                    concour = new_concour,
                    note = new_note
                )
            else : 
                print("false cne")  
            new_inscription.save()
            
            messages.success(request, 'Vous avez inscris avec succès.')
            return redirect('concour')
    else:
        form = inscri_concour()
    return render(request, 'student/inscription.html',{
            'form': form
        })

