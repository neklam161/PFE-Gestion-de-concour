from django.db import models
from datetime import datetime, date

from django.contrib.auth.models import User

class Etudiant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    cne = models.CharField(max_length=12,primary_key=True,unique=True)
    nom = models.CharField(max_length=12)
    prenom = models.CharField(max_length=12)
    email = models.EmailField(max_length=30,unique=True)
    password=models.CharField(max_length=100,blank=True, null=True)
    confirmpassword=models.CharField(max_length=50,null=True)
    DateNaissance = models.DateField()
    Numerotelephone = models.IntegerField()

    def __str__(self):
        return self.cne
    class Meta:
        db_table = 'Student'
    