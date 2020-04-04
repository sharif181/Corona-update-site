from django.db import models

class info(models.Model):
    number_of_infected = models.IntegerField()
    number_of_death = models.IntegerField()
    number_of_survive = models.IntegerField()

class worldInfo(models.Model):
    number_of_infected = models.IntegerField()
    number_of_death = models.IntegerField()
    number_of_survive = models.IntegerField()