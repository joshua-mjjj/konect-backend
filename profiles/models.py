from django.db import models
from django.contrib.auth.models import User


def upload_path(instance, filname):
    return '/'.join(['profile_pictures', str(instance.owner), filname])

class serviceProvider(models.Model):
	lat = models.FloatField(max_length=9)
	lon = models.FloatField(max_length=9)
	services = models.CharField(max_length=150)
	contact = models.CharField(max_length=10)
	email = models.EmailField(max_length=100, null=True,blank=True)
	other = models.CharField(max_length=100)
	profile_picture = models.ImageField(blank=True, null=True, upload_to=upload_path)
	owner = models.ForeignKey(
	    User, related_name="profiles", 
	    on_delete=models.CASCADE, null=True)

	def __str__(self):
		return '{} {}'.format(self.owner, self.services)
