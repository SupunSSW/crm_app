from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    website = models.CharField(max_length=100)


class Employee(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    comp = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    tele = models.CharField(max_length=50)