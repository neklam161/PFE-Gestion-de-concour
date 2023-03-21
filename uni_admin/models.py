from django.db import models
from student.models import concours,university

from django.contrib.auth.models import User
# Create your models here.
class University_admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='university_admin', null=True)
    cin = models.CharField(max_length=12,primary_key=True,unique=True)
    university = models.ForeignKey(university,on_delete=models.CASCADE,null=False)
    nom = models.CharField(max_length=12)
    prenom = models.CharField(max_length=12)
    email = models.EmailField(max_length=30,unique=True)
    password=models.CharField(max_length=50,blank=True, null=True)
    confirmpassword=models.CharField(max_length=50,null=True)
    DateNaissance = models.DateField()
    Numerotelephone = models.IntegerField()

    def __str__(self):
        return self.cin
    class Meta:
        db_table = 'university_admin'