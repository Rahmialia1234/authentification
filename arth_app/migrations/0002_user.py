# Generated by Django 5.0.6 on 2024-05-18 16:37

import django
from django.db import migrations, models
import datetime
import django.db.models.deletion

class Migration(migrations.Migration):
    initial = True
    dependencies = [
        ('arth_app', '0001_initial'),]
    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=20)),
                ('uname', models.CharField(max_length=100)),
                ('uprenom', models.CharField(max_length=100)),
                ('departement', models.CharField(max_length=100)),
                ('uemail', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=50)),
            ], ),
 
       
     ]
