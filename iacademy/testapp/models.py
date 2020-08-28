from django.db import models

# Create your models here.


class Tutors(models.Model):
    name = models.CharField(max_length=50)
    cellno = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class Students(models.Model):
    name = models.CharField(max_length=50)
    fathername = models.CharField(max_length=50)
    area = models.CharField(max_length=50)
    cellno = models.IntegerField()
    email = models.EmailField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name