from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class MyCustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Etudiant(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cne = models.CharField(max_length=12, primary_key=True, unique=True)
    nom = models.CharField(max_length=12)
    prenom = models.CharField(max_length=12)
    email = models.EmailField(max_length=30, unique=True)
    password = models.CharField(max_length=100, blank=True, null=True)
    confirmpassword = models.CharField(max_length=100, null=True)
    DateNaissance = models.DateField()
    lieu_naissance = models.CharField(max_length=50, null=True)
    pays_naissance = models.CharField(max_length=50, null=True)
    nationalite = models.CharField(max_length=50, null=True)
    sexe = models.CharField(max_length=10, null=True, choices=[('Masculin', 'Masculin'), ('Feminin', 'Feminin')])
    situation_familiale = models.CharField(max_length=30, null=True, choices=[('Celibataire', 'Celibataire'), ('Marie', 'Marie'),('Divorce', 'Divorce')])
    adresse = models.CharField(max_length=200, null=True)
    serie_bac = models.CharField(max_length=10, null=True,choices=[(str(i)+"-"+str(i+1),str(i)+"-"+str(i+1)) for i in range(2010,2020)])
    mention_bac = models.CharField(max_length=20, null=True,choices=[("Bien","Bien"),("Tres Bien","Tres Bien"),("Assez Bien","Assez Bien")])
    province_bac = models.CharField(max_length=50, null=True)
    diplome= models.CharField(max_length=10, null=True, choices=[('DUT', 'DUT'), ('DEUG', 'DEUG'),("Licence","Licence")])
    Etablissement=models.CharField(max_length=200,null=True)
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
    

class etablissement(models.Model):
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
    note = models.IntegerField(null=True,blank=True)
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
