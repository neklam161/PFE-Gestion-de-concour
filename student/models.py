from django.db import models
from datetime import datetime, date


class Etudiant(models.Model):
    cne = models.CharField(max_length=12,primary_key=True)
    nom = models.CharField(max_length=12)
    prenom = models.CharField(max_length=12)
    email = models.EmailField(max_length=30)
    password=models.CharField(max_length=50,blank=True, null=True)
    confirmpassword=models.CharField(max_length=50,null=True)
    DateNaissance = models.DateField()
    Numerotelephone = models.IntegerField()
    def __str__(self):
        return self.cne
