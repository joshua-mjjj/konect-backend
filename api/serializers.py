from rest_framework import serializers

from .models import *

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class ServiceProvider_Motor_Serializer(serializers.ModelSerializer):
	class Meta:
		model = ServiceProvider_Motor
		fields = '__all__'

class Motor_SerializerCordinates(serializers.ModelSerializer):
	class Meta:
		model = ServiceProvider_Motor
		fields = ('lat', 'lon', 'cordinate')

class User_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Client
		fields = '__all__'

class UserCordinates_Serializer(serializers.ModelSerializer):
	class Meta:
		model = Client
		fields = ('lat', 'lon', 'cordinate')