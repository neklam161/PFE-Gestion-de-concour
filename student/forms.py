from django import forms
from .models import Etudiant

class EtudiantForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Etudiant
        fields = ["cne" ,"nom" , "prenom" ,"email" ,"password", "DateNaissance","Numerotelephone"]
        label = {
            "cne": "CNE", 
            "nom":"Nom" , 
            "prenom" :"Prenom",
            "email":"Address Electronique",
            "password":"Mot de Pass", 
            "DateNaissance":"Date de Naissance",
            "Numerotelephone": "Numero de telephone"
        }
        widget = {
            "cne":forms.TextInput(attrs={'class':'form-control'}) ,
            "nom":forms.TextInput(attrs={'class':'form-control'}) ,
             "prenom":forms.TextInput(attrs={'class':'form-control'}) ,
             "email":forms.EmailInput(attrs={'class':'form-control'}),
             "password":forms.PasswordInput(attrs={'class':'form-control'}),
              "DateNaissance":forms.DateField(),  
             "Numerotelephone": forms.NumberInput(attrs={'class':'form-control'})
        }