from django.shortcuts import render
from .forms import EtudiantForm
from .models import Etudiant
# Create your views here.
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