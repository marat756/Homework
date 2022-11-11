from django.db import models

class Car(models.Model):
    nomi = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    narxi = models.IntegerField()


class Traktor(models.Model):
    nomi = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    narxi = models.IntegerField()


class Kamaz(models.Model):
    nomi = models.CharField(max_length=30)
    model = models.CharField(max_length=30)
    narxi = models.IntegerField()

def __str__(self):
    return f"{self.nomi} {self.narxi}"
