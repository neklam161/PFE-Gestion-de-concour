from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

from django.contrib import messages
from .forms import *
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.serializers.json import DjangoJSONEncoder
import json
import hashlib
@csrf_protect
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            print(f"Email: {email}, Password: {password}, Hashed Password: {hashed_password}")
            user = authenticate(request, email=email, password=hashed_password)
            if user is not None:
                login(request, user)
                if hasattr(user, 'etudiant'):
                    return redirect("studentpage")
                elif hasattr(user, 'university_admin'):
                    return redirect("concour")
            else:
                print("none")
                return render(request, 'student/login.html', {'form': form, 'error': 'Invalid email or password.'})
 
    else:
        print("testt")
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
               #confirmpassword = new_confpassword,
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


def form_step1(request):
    if request.method == 'POST':
        form = EtudiantFormStep1(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            form.cleaned_data['password'] = hashed_password

            confirmpassword = form.cleaned_data['confirmpassword']
            hashed_confirmpassword = hashlib.sha256(confirmpassword.encode('utf-8')).hexdigest()
            form.cleaned_data['confirmpassword'] = hashed_confirmpassword

            form.cleaned_data['DateNaissance'] = str(form.cleaned_data['DateNaissance'])
            request.session['step1_data'] = json.dumps(form.cleaned_data, cls=DjangoJSONEncoder)
            return redirect('form_step2')
    else:
        form = EtudiantFormStep1()
    return render(request, 'student/form_step1.html', {'form': form})


def form_step2(request):
    if request.method == 'POST':
        form = EtudiantFormStep2(request.POST)
        if form.is_valid():
            request.session['step2_data'] = form.cleaned_data
            return redirect('form_step3')
    else:
        form = EtudiantFormStep2()
    return render(request, 'student/form_step2.html', {'form': form})

def form_step3(request):
    if request.method == 'POST':
        form = EtudiantFormStep3(request.POST)
        if form.is_valid():
            # Store the form data in the session
            request.session['step3_data'] = json.dumps(form.cleaned_data, cls=DjangoJSONEncoder)
            return redirect('form_step4')
    else:
        form = EtudiantFormStep3()

    # Retrieve the step1_data and step2_data from the session
    step1_data = json.loads(request.session.get('step1_data', '{}'))
    step2_data = request.session.get('step2_data', {})

    # Merge the form data from all steps
    etudiant_data = {**step1_data, **step2_data}

    # Retrieve the step3_data from the session and merge it with etudiant_data
    step3_data = request.session.get('step3_data', {})
    if step3_data:
        etudiant_data = {**etudiant_data, **json.loads(step3_data)}

    return render(request, 'student/form_step3.html', {'form': form})





def form_step4(request):
    if request.method == 'POST':
        form = EtudiantFormStep4(request.POST)
        if form.is_valid():
            step1_data = request.session.get('step1_data')
            step2_data = request.session.get('step2_data')
            step3_data = json.loads(request.session.get('step3_data', {}))

            if step1_data and step2_data:
                # Combine data from all previous steps with step 4 data
                etudiant_data = {**json.loads(step1_data), **step2_data, **step3_data, **form.cleaned_data}
                
                # Create a new MyCustomUser object and set its username and password fields
                mycustomuser = MyCustomUser.objects.create_user(
                    email=etudiant_data['email'],
                     password=etudiant_data['password']
                    )
                
                
                # Associate the MyCustomUser object with the Etudiant object
                etudiant_data['user'] = mycustomuser
                
                # Create a new Etudiant object
                etudiant = Etudiant.objects.create(**etudiant_data)
                
                # Clear session data after creating the Etudiant object
                request.session.flush()
                
                # Redirect to a success page or any other page you'd like
                return redirect('login')
    else:
        form = EtudiantFormStep4()
    return render(request, 'student/form_step4.html', {'form': form})


