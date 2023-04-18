from django.db import models


class Traduction(models.Model):
    francais = models.CharField(max_length=255)
    soninke = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.francais} -> {self.soninke}"
