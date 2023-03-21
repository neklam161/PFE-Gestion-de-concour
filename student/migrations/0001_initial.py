# Generated by Django 4.1.6 on 2023-03-17 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='concours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('doc_necessaire', models.CharField(max_length=300)),
                ('filliere', models.CharField(max_length=300)),
                ('seuille', models.IntegerField()),
                ('n_place', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('cne', models.CharField(max_length=12, primary_key=True, serialize=False, unique=True)),
                ('nom', models.CharField(max_length=12)),
                ('prenom', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
                ('confirmpassword', models.CharField(max_length=50, null=True)),
                ('DateNaissance', models.DateField()),
                ('Numerotelephone', models.IntegerField()),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='etudiant', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Student',
            },
        ),
        migrations.CreateModel(
            name='university',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='refus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.IntegerField()),
                ('concour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.concours')),
                ('etudiant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.etudiant')),
            ],
            options={
                'ordering': ['-note'],
            },
        ),
        migrations.AddField(
            model_name='concours',
            name='university',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.university'),
        ),
        migrations.CreateModel(
            name='attente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classement', models.IntegerField(blank=True, null=True)),
                ('note', models.IntegerField()),
                ('date_creation', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('A', 'Admis'), ('R', 'Refus')], max_length=1)),
                ('concour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.concours')),
                ('etudiant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.etudiant')),
            ],
            options={
                'ordering': ['-note', 'date_creation'],
            },
        ),
        migrations.CreateModel(
            name='admis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.IntegerField()),
                ('concour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.concours')),
                ('etudiant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.etudiant')),
            ],
            options={
                'ordering': ['-note'],
            },
        ),
    ]
