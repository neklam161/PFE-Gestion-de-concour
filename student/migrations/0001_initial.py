# Generated by Django 4.1.6 on 2023-02-26 18:02

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
            name='Etudiant',
            fields=[
                ('cne', models.CharField(max_length=12, primary_key=True, serialize=False, unique=True)),
                ('nom', models.CharField(max_length=12)),
                ('prenom', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('confirmpassword', models.CharField(max_length=50, null=True)),
                ('DateNaissance', models.DateField()),
                ('Numerotelephone', models.IntegerField()),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Student',
            },
        ),
    ]
