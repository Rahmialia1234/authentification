from django.db import models


class Utilisateur(models.Model):
    nom = models.CharField(max_length=50)
    mot_de_passe = models.CharField(max_length=50)


class User(models.Model):
      uid = models.CharField(max_length=20)
      uname = models.CharField(max_length=100)
      uprenom = models.CharField(max_length=100)
      departement = models.CharField(max_length=100)
      uemail = models.EmailField()
      telephone = models.CharField(max_length=50)

class Meta:
     db_table = "user"


