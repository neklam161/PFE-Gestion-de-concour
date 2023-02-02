# Generated by Django 4.1.6 on 2023-02-02 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('cne', models.CharField(max_length=12, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=12)),
                ('prenom', models.CharField(max_length=12)),
                ('email', models.EmailField(blank=True, max_length=30, null=True)),
                ('password', models.CharField(max_length=50)),
                ('DateNaissance', models.DateField()),
                ('Numerotelephone', models.IntegerField()),
            ],
        ),
    ]
