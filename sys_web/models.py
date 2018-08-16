from django.db import models

# Create your models here.


class Dados(models.Model):
    criterio1 = models.CharField(max_length=20)
    criterio2 = models.CharField(max_length=20)
    criterio3 = models.CharField(max_length=20)

    decisor1 = models.CharField(max_length=20)
    decisor2 = models.CharField(max_length=20)
    decisor3 = models.CharField(max_length=20)

    alternativa1 = models.CharField(max_length=20)
    alternativa2 = models.CharField(max_length=20)
    alternativa3 = models.CharField(max_length=20)



class Criterios(models.Model):
    d1c1c2 = models.IntegerField()
    d1c1c3 = models.IntegerField()
    d1c2c3 = models.IntegerField()

    d2c1c2 = models.IntegerField()
    d2c1c3 = models.IntegerField()
    d2c2c3 = models.IntegerField()

    d3c1c2 = models.IntegerField()
    d3c1c3 = models.IntegerField()
    d3c2c3 = models.IntegerField()

class Avaliarum(models.Model):
    c1a1a2 = models.IntegerField()
    c1a1a3 = models.IntegerField()
    c1a2a3 = models.IntegerField()

    c2a1a2 = models.IntegerField()
    c2a1a3 = models.IntegerField()
    c2a2a3 = models.IntegerField()

    c3a1a2 = models.IntegerField()
    c3a1a3 = models.IntegerField()
    c3a2a3 = models.IntegerField()

class Avaliardois(models.Model):
    c1a1a2 = models.IntegerField()
    c1a1a3 = models.IntegerField()
    c1a2a3 = models.IntegerField()

    c2a1a2 = models.IntegerField()
    c2a1a3 = models.IntegerField()
    c2a2a3 = models.IntegerField()

    c3a1a2 = models.IntegerField()
    c3a1a3 = models.IntegerField()
    c3a2a3 = models.IntegerField()

class Avaliartres(models.Model):
    c1a1a2 = models.IntegerField()
    c1a1a3 = models.IntegerField()
    c1a2a3 = models.IntegerField()

    c2a1a2 = models.IntegerField()
    c2a1a3 = models.IntegerField()
    c2a2a3 = models.IntegerField()

    c3a1a2 = models.IntegerField()
    c3a1a3 = models.IntegerField()
    c3a2a3 = models.IntegerField()
