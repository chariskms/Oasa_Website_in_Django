from django.contrib.auth.models import User, Group
from django.db import models

# Create your models here.


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Elder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Unemployed(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Normal(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Resellers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Station(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    area = models.CharField(max_length=100, blank=False)

    class Meta:
        unique_together = (("name", "area"),)

    def __str__(self):
        return self.name


class MetroLine(models.Model):
    id = models.IntegerField(primary_key=True)
    stations = models.ManyToManyField(Station)
    terminalStation1 = models.CharField(max_length=100, blank=False)
    terminalStation2 = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return str(self.id)


class BusLine(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    stations = models.ManyToManyField(Station)
    terminalStation1 = models.CharField(max_length=100, blank=False)
    terminalStation2 = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name



class TramLine(models.Model):
    id = models.IntegerField(primary_key=True)
    stations = models.ManyToManyField(Station)
    terminalStation1 = models.CharField(max_length=100, blank=False)
    terminalStation2 = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return str(self.id)



