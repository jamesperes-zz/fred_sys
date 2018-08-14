from django.db import models

# Create your models here.


class Criterio(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Decisor(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Alternativa(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class AlternativaValor(models.Model):
    valor = models.IntegerField()
    nome_alternativa = models.ManyToManyField(Alternativa)


class Contador(models.Model):
    grupo_criterio = models.ManyToManyField(Criterio)
    grupo_decisor = models.ManyToManyField(Decisor)
