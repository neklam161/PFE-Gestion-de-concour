from django.db import models
from datetime import datetime, date

from django.contrib.auth.models import User

class Etudiant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    cne = models.CharField(max_length=12,primary_key=True,unique=True)
    nom = models.CharField(max_length=12)
    prenom = models.CharField(max_length=12)
    email = models.EmailField(max_length=30,unique=True)
    password=models.CharField(max_length=50,blank=True, null=True)
    confirmpassword=models.CharField(max_length=50,null=True)
    DateNaissance = models.DateField()
    Numerotelephone = models.IntegerField()

    def __str__(self):
        return self.cne
    class Meta:
        db_table = 'Student'
    

class university(models.Model):
    id = models.CharField(primary_key=True,max_length=30)
    name = models.CharField(max_length=200) 
    location = models.CharField(max_length=30)
    def _str_(self):
        return self.name


class concours(models.Model):
    name = models.CharField(max_length=200)
    university = models.ForeignKey(university, on_delete=models.CASCADE,null=True )
    description = models.CharField(max_length=300)
    start_date = models.DateField()
    end_date = models.DateField()
    doc_necessaire = models.CharField(max_length=300)


    def _str_(self):
        return self.name 