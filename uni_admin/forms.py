from django import forms
from .models import *
from student.models import concours
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password
from django.contrib.admin.widgets import AdminDateWidget

class DateInput(forms.DateInput):
    input_type = 'date'

class add_Concour(forms.ModelForm):
    name = forms.CharField()
    #university = forms.CharField()
    description = forms.CharField(widget=forms.Textarea(attrs={'name':'body', 'rows':3, 'cols':5}))
    start_date = forms.DateField(widget=DateInput)
    end_date = forms.DateField(widget=DateInput)
    doc_necessaire = forms.CharField()
    #location=forms.CharField()
    filliere = forms.CharField()
    seuille = forms.IntegerField()
    n_place = forms.IntegerField()
    
    class Meta:
        model = concours
        fields = ['name', 'description', 'start_date', 'end_date', 'doc_necessaire' , 'seuille' , 'filliere' , 'n_place']
        