from django.db import models
from datetime import datetime

# Create your models here.
class Club(models.Model):
    nom = models.CharField(max_length=255)
    ville = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255, null=True)
    mail = models.CharField(max_length=255, null=True)
    president_nom = models.CharField(max_length=255, null=True)
    president_prenom = models.CharField(max_length=255, null=True)


class Equipe(models.Model):
    # club foreign key to Club
    CATEGORIES = (
        ('U7', 'Baby'),
        ('U9', 'Mini-Poussin'),
        ('U11', 'Poussin'),
        ('U13', 'Benjamin'),
        ('U15', 'Minime'),
        ('U17', 'Cadet'),
        ('U20', 'Junior'),
        ('S', 'Senior'),
    )
    categorie = models.CharField(max_length=1, choices=CATEGORIES)
    annee = models.PositiveIntegerField(max_length=4, default=int(datetime.now().year))
    # coach foreign key to Coach


class Coach(models.Model):
    nom = CharField(max_length=255)
    prenom = CharField(max_length=255)


class Joueur(models.Model):
    nom =
    prenom =
    taille_cm =
    poids =
    date_de_naissance =
    poste =
    numero =
    photo =

    
class Match(models.Model):
class Statistique(models.Model):
