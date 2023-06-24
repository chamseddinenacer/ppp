from django.db import models
from PIL import Image
from django.utils import timezone


class Animauxlost(models.Model):

    userlost = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    bred = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.IntegerField()
    descri = models.TextField()
    couleur = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    distmarkings = models.CharField(max_length=100)
    image = models.ImageField(upload_to='animaux_images_lost/')
    # datelost = models.DateTimeField(auto_now_add=True)
    datelost = models.DateTimeField(default=timezone.now)
    addrs = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Animauxfound(models.Model):
    
    userfound = models.CharField(max_length=100)
    bred = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.IntegerField()
    descri = models.TextField()
    couleur = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    distmarkings = models.CharField(max_length=100)
    image = models.ImageField(upload_to='animaux_images_found/')
    datefound = models.DateTimeField(default=timezone.now)
    addrs = models.CharField(max_length=100)

    def __str__(self):
        return self.couleur     


 
class Animaux(models.Model):

    useridan = models.CharField(max_length=100)
    name = models.CharField(max_length=100, default='')
    bred = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.IntegerField()
    descri = models.TextField()
    couleur = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    distmarkings = models.CharField(max_length=100)
    daten = models.DateTimeField(default=timezone.now)
    addrs = models.CharField(max_length=100)
    image = models.ImageField(upload_to='animaux_images/')


    def __str__(self):
        return self.name



class Favorite(models.Model):

    userid = models.CharField(max_length=100)
    animid = models.CharField(max_length=100)
    

    def __str__(self):
        return self.animid