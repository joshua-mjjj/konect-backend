from django.db import models
from django.contrib.auth.models import User

class serviceProvider(models.Model):
	lat = models.FloatField(max_length=9)
	lon = models.FloatField(max_length=9)
	services = models.CharField(max_length=150)
	contact = models.CharField(max_length=10)
	email = models.EmailField(max_length=100, null=True,blank=True)
	other = models.CharField(max_length=100)
	owner = models.ForeignKey(
	    User, related_name="profiles", 
	    on_delete=models.CASCADE, null=True)

	def __str__(self):
		return '{} {}'.format(self.owner, self.services)
