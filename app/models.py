from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone


class Usuario(models.Model):

	email = models.EmailField(max_length=75)
	nombre = models.CharField(max_length = 140)
	status = models.BooleanField(default = False)
	tel = models.CharField(max_length = 140)

	def __str__(self):
		return "%s - %s" % (self.nombre,self.status)


class TipoNegocio(models.Model):

	tiponegocio = models.CharField(max_length = 140)

	def __str__(self):
		return self.tiponegocio

class Ciudad(models.Model):

	nombre = models.CharField(max_length = 140)


	def __str__(self):
		return self.nombre



class Negocio(models.Model):

	ciudad = models.ForeignKey(Ciudad)
	direccion = models.CharField(max_length = 140)
	email = models.EmailField(max_length=75)
	logo = models.ImageField(upload_to = True)
	nombre = models.CharField(max_length = 140)
	status = models.BooleanField(default = False)
	tel = models.CharField(max_length = 140)
	tiponegocio = models.ForeignKey(TipoNegocio)

	def __str__(self):
		return self.nombre


class Album(models.Model):

	nombre = models.CharField(max_length = 140)

	negocio = models.ForeignKey(Negocio)

	def __str__(self):
		return self.nombre


class Foto(models.Model):

	album = models.ForeignKey(Album)
	timestamp = models.DateTimeField(auto_now = True)
	files =  models.ImageField(upload_to = True)

	def __str__(self):
		return "%s" % (self.timestamp)
