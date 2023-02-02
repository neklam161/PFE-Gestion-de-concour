from django.db import models
from datetime import datetime, date

# Create your models here.
class Etudiant(models.Model):
    cne = models.CharField(max_length=12,primary_key=True)
    nom = models.CharField(max_length=12)
    prenom = models.CharField(max_length=12)
    email = models.EmailField(max_length=30, blank=True, null=True)
    password=models.CharField(max_length=50)
    DateNaissance = models.DateField()
    Numerotelephone = models.IntegerField()
