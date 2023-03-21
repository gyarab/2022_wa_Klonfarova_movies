from django.db import models

# Create your models here.


class Movie(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField( blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    director = models.ForeignKey('Director', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name} ({self.year})"

class Director(models.Model):
    name = models.CharField(max_length=255)
    birth_year = models.IntegerField()
    