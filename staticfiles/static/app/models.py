from django.db import models


class Traduction(models.Model):
    francais = models.CharField(max_length=255,db_index=True)
    soninke = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.francais} -> {self.soninke}"

from django.db import models

class Contribution(models.Model):
    nom_complet = models.CharField(max_length=30)
    francais = models.CharField(max_length=30)
    soninke = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.nom_complet}: {self.francais} -> {self.soninke}"
