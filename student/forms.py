from django import forms
from .models import Etudiant
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password



class DateInput(forms.DateInput):
    input_type = 'date'  

class EtudiantForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirmpassword=forms.CharField(widget=forms.PasswordInput())
    DateNaissance=forms.DateField(widget=DateInput)
    class Meta:
        model = Etudiant
        fields = ["cne" ,"nom" , "prenom" ,"email" ,"password","confirmpassword", "DateNaissance","Numerotelephone"]
    def clean(self):
        cleaned_data = super().clean()
        vpassword = self.cleaned_data["password"]
        vconfirmpassword = self.cleaned_data["confirmpassword"]

        if vpassword != vconfirmpassword:
            print("working")
            raise forms.ValidationError(
            "password and confirm_password does not match"
            )
 

    def check_email_exists(email):
        try:
            Etudiant.objects.get(email=email)
            raise ValidationError('This email is already in use.')
        except Etudiant.DoesNotExist:
            pass
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.password = make_password(self.cleaned_data["password"])
        if commit:
            instance.save()
        return instance

    label = {
            "cne": "CNE", 
            "nom":"Nom" , 
            "prenom" :"Prenom",
            "email":"Address Electronique",
            "password":"Mot de Pass", 
            "confirmpassword":"Confirmer votre Mot de Pass",
            "DateNaissance":"Date de Naissance",
            "Numerotelephone": "Numero de telephone"
        }
    widget = {
            "cne":forms.TextInput(attrs={'class':"form-control"}) ,
            "nom":forms.TextInput(attrs={'class':"form-control"}) ,
             "prenom":forms.TextInput(attrs={'class':"form-control"}) ,
             "email":forms.EmailInput(attrs={'class':"form-control"}),
             "password":forms.PasswordInput(attrs={'class':"form-control"}),
             "confirmpassword":forms.PasswordInput(attrs={'class':"form-control"}),
              "DateNaissance":forms.DateInput(),  
             "Numerotelephone": forms.NumberInput(attrs={'class':"form-control"})
        }

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'example@gmail.com'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    
    
class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-input', 'placeholder': 'Search anything...'}))    


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ['nom', 'prenom', 'cne', 'email', 'DateNaissance', 'Numerotelephone', 'profile_pic']

    profile_pic = forms.ImageField(label='Profile Picture', required=False)
