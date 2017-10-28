# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class TipoCuenta(models.Model):
	nom_tipo = models.CharField(max_length=50)
	codigo_tcuenta = models.CharField(max_length=1, primary_key=True)
	disminuye_en = models.CharField(max_length=10)
	aumenta_en = models.CharField(max_length=10)

class GrupoCuenta(models.Model):
	tipo_cuenta = models.OneToOneField(TipoCuenta)
	nom_grupo = models.CharField(max_length=50, blank=False, unique=True)
	codigo_gcuenta = models.CharField(max_length=2, blank=False, unique=True, primary_key=True)
	descripcion = models.CharField(max_length=200, blank=False)

class Cuenta(models.Model):
	grupo = models.ForeignKey(GrupoCuenta, blank=False)
	nom_cuenta = models.CharField(max_length=100, blank=False, unique=True)
	descripcion = models.CharField(max_length=200, blank=False)
	codigo_cuenta = models.CharField(max_length=3, blank=False, unique=True, primary_key=True)
	cuenta_padre = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True
    )

class PeriodoContable(models.Model):
	fecha_inicio = models.DateField()
	fecha_final = models.DateField()
	usr_aperturo = models.CharField(max_length=20, blank=False)
	usr_cerro = models.CharField(max_length=20, blank=False)

class LibroMayor(models.Model):
	cuenta = models.ForeignKey(Cuenta, blank=False, null=False)
	debe = models.FloatField()
	haber = models.FloatField()
	fecha = models.DateField(blank=False)

class Diario(models.Model):
	periodo = models.ForeignKey(PeriodoContable, blank=False, null=False)
	libro_mayor = models.ForeignKey(LibroMayor, blank=False, null=False)
	debe = models.FloatField()
	haber = models.FloatField()
	descripcion = models.CharField(max_length=200)
	fecha = models.DateField(blank=False)
	autorizo = models.CharField(max_length=200, blank=False)

class DocLibro(models.Model):
	diario = models.ForeignKey(Diario, blank=False, null=False)
	cuenta = models.ForeignKey(Cuenta, blank=False, null=False)
	concepto = models.CharField(max_length=20, blank=False)
	debe = models.FloatField()
	haber = models.FloatField()
