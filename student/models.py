from django.db import models

from django.contrib.auth.models import User


class Etudiant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name='etudiant')
    cne = models.CharField(max_length=12, primary_key=True, unique=True)
    nom = models.CharField(max_length=12)
    prenom = models.CharField(max_length=12)
    email = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    confirmpassword = models.CharField(max_length=50, null=True)
    DateNaissance = models.DateField()
    Numerotelephone = models.IntegerField()
    profile_pic = models.ImageField(upload_to='student/img', default='student/img/user.png')

    def __str__(self):
        return self.prenom

    class Meta:
        db_table = 'Student'


class university(models.Model):
    id = models.CharField(primary_key=True,max_length=30)
    name = models.CharField(max_length=200) 
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class etablissement():
    university = models.ForeignKey(university, on_delete=models.CASCADE,null=True )
    name = models.CharField(max_length=200) 
    description = models.CharField(max_length=300)




class concours(models.Model):
    #name = models.CharField(max_length=200)
    etablissement = models.ForeignKey(etablissement, on_delete=models.CASCADE,null=True )
    #description = models.CharField(max_length=300)
    start_date = models.DateField()
    end_date = models.DateField()
    #doc_necessaire = models.CharField(max_length=300)
    filliere = models.CharField(max_length=300)
    seuille =models.IntegerField()
    #n_place=models.IntegerField()


    def __str__(self):
        return self.name 
    

class attente(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE,null=True)
    concour = models.ForeignKey(concours, on_delete=models.CASCADE,null=True)
    classement = models.IntegerField(null=True,blank=True)
    note = etudiant.note
    date_creation = models.DateTimeField(auto_now_add=True)
    
    STATUS_CHOICES = [
        ('A', 'Admis'),
        ('R', 'Refus'),
    ]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,null=True)


    class Meta:
        ordering = ['-note', 'date_creation']
    
    

    def save(self, *args, **kwargs):
        
        if not self.classement:
            higher_notes = attente.objects.filter(note__gt=self.note)
  
            same_notes = higher_notes.filter(note=self.note, date_creation__lt=self.date_creation)

            for instance in higher_notes:
                instance.classement += 1
                instance.save()

            self.classement = higher_notes.count() + 1 - same_notes.count()

        super(attente, self).save(*args, **kwargs)
