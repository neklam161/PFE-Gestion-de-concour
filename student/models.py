from django.db import models

from django.contrib.auth.models import User
from django.utils import timezone

class Etudiant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,related_name='etudiant')
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
    filliere = models.CharField(max_length=300)
    seuille =models.IntegerField()
    n_place=models.IntegerField()


    def str(self):
        return self.name 
    

class attente(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE,null=True)
    concour = models.ForeignKey(concours, on_delete=models.CASCADE,null=True)
    classement = models.IntegerField(null=True,blank=True)
    note = models.IntegerField()
    date_creation = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = [
        ('A', 'Admis'),
        ('R', 'Refus'),
    ]
    class Meta:
        ordering = ['-note', 'date_creation']
    
   
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def set_status(self):
        if self.concour.end_date < timezone.now():
            if self.classement is not None and self.classement <= self.concour.n_place:
                self.status = 'A'
            else:
                self.status = 'R'
    

    def save(self, *args, **kwargs):
        # Check if classement is already set
        if not self.classement:
            # Get all instances of this model with a higher note value
            higher_notes = attente.objects.filter(note__gt=self.note)

            # Filter instances with the same note value and an older creation date
            same_notes = higher_notes.filter(note=self.note, date_creation__lt=self.date_creation)

            # Increment the classement of each instance with a higher note value
            for instance in higher_notes:
                instance.classement += 1
                instance.save()

            # Set the classement attribute of the current instance
            self.classement = higher_notes.count() + 1 - same_notes.count()

        super(attente, self).save(*args, **kwargs)



class admis(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE,null=True)
    concour = models.ForeignKey(concours, on_delete=models.CASCADE,null=True)
    note = models.IntegerField()

    class Meta:
        ordering = ['-note']




class refus(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE,null=True)
    concour = models.ForeignKey(concours, on_delete=models.CASCADE,null=True)
    note = models.IntegerField()
    class Meta:
        ordering = ['-note']