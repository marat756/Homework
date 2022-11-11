from django.db import models

class Telepon(models.Model):
    nomi = models.CharField(max_length=30)
    model = models.TextField()
    narxi = models.IntegerField()

class Apple(models.Model):
    nomi = models.CharField(max_length=30)
    model = models.TextField()
    narxi = models.IntegerField()


class Notebook(models.Model):
    nomi = models.CharField(max_length=30)
    model = models.TextField()
    narxi = models.IntegerField()



def __str__(self):
    return f"{self.nomi} {self.narxi}"
