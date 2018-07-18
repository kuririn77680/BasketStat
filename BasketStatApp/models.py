from django.db import models
from datetime import datetime

# Create your models here.
class Club(models.Model):
    # 1 club possede 0 a x Equipe
    nom = models.CharField(max_length=255, unique=True)
    ville = models.CharField(max_length=255, null=True)
    telephone = models.CharField(max_length=255, null=True)
    mail = models.CharField(max_length=255, null=True)
    president_nom = models.CharField(max_length=255, null=True)
    president_prenom = models.CharField(max_length=255, null=True)


class Equipe(models.Model):
    # equipe appartient a 1 unique Club
    # une equipe possede 0 a x coachs
    # une equipe possede à a x joueurs
    # une equipe possede à a x matchs
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
    # joueurs foreign key to Joueur


class Coach(models.Model):
    # 1 coach peut entrainer à a x equipe
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)


class Joueur(models.Model):
    # 1 joueur appartient 0:X equipe
    # 1 joueur possede 0:X stats
    POSTE = (
        ('MJ', 'Meneur de Jeu'),
        ('A', 'Arrière'),
        ('AL', 'Aillier'),
        ('AF', 'Aillier Fort'),
        ('P', 'Pivot'),
    )
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    taille_cm = models.PositiveIntegerField(default=1, null=True)
    poids = models.PositiveIntegerField(default=1, null=True)
    date_de_naissance = models.DateField(null=True)
    poste = models.CharField(max=1, choices=POSTE)
    numero =  models.PositiveIntegerField(default=1, null=True)
    photo = models.ImageField(upload_to=get_image_path, blank=True, null=True)


class Match(models.Model):
    # 1 match appartient a 1 equipe
    domicile = models.BooleanField(default=True)
    adversaire = models.CharField(max_length=255)
    date = models.DateField(default=datetime.date.today)
    victoire = models.BooleanField(default=False, null=True)
    score_dom = models.PositiveIntegerField(default=0, null=True)
    score_ext = models.PositiveIntegerField(default=0, null=True)


class Statistique(models.Model):
    # 1 stat appartient a 1 joueur
    temps = models.PositiveIntegerField(default=0)
    lf_mis = models.PositiveIntegerField(default=0)
    lf_tente = models.PositiveIntegerField(default=0)
    pts2_mis = models.PositiveIntegerField(default=0)
    pts2_tente = models.PositiveIntegerField(default=0)
    pts3_mis = models.PositiveIntegerField(default=0)
    pts3_tente = models.PositiveIntegerField(default=0)
    passe_decisive = models.PositiveIntegerField(default=0)
    interception = models.PositiveIntegerField(default=0)
    rebond_off = models.PositiveIntegerField(default=0)
    rebonf_def = models.PositiveIntegerField(default=0)
    perte_de_balle = models.PositiveIntegerField(default=0)
    contre = models.PositiveIntegerField(default=0)
    contre_subis = models.PositiveIntegerField(default=0)
