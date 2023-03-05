# Generated by Django 4.1.6 on 2023-03-05 19:08

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
            name='university',
            fields=[
                ('id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=30)),
            ],
        ),
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
        migrations.CreateModel(
            name='concours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=300)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('doc_necessaire', models.CharField(max_length=300)),
                ('university', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.university')),
            ],
        ),
    ]
