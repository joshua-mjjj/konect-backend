from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

from django.contrib.auth.models import User

class Client(models.Model):
	lat = models.FloatField(max_length=9)
	lon = models.FloatField(max_length=9)
	cordinate = models.CharField(max_length=100, editable=False)
	neighbours = models.PositiveIntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(7)])
	name = models.CharField(max_length=70)
	need = models.CharField(max_length=200)

	def save(self, *args, **kwargs):
		self.cordinate = list()
		self.cordinate.append(self.lat)
		self.cordinate.append(self.lon)

		# print(self.cordinate)
		# print(self.cordinate[0])
		# print(self.cordinate[1])
		
		super(Client, self).save(*args, **kwargs)

	def __str__(self):
		return '{} {} {}'.format(self.name, self.neighbours, self.cordinate)

class ServiceProvider_Motor(models.Model):
	lat = models.FloatField(max_length=9)
	lon = models.FloatField(max_length=9)
	cordinate = models.CharField(max_length=100, editable=False)
	name = models.CharField(max_length=70)
	services = models.CharField(max_length=150)
	contact = models.CharField(max_length=10)
	email = models.EmailField(max_length=100)
	other = models.CharField(max_length=100)

	def save(self, *args, **kwargs):
		self.cordinate = list()
		self.cordinate.append(self.lat)
		self.cordinate.append(self.lon)
		super(ServiceProvider_Motor, self).save(*args, **kwargs)

	def __str__(self):
		return '{} {} {}'.format(self.name, self.contact, self.cordinate)




