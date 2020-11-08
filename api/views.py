from django.shortcuts import render
from django.http import JsonResponse
from math import sqrt, radians, cos, sin, asin, degrees, atan2
import numpy as np


from rest_framework.decorators import api_view, throttle_classes
from rest_framework.response import Response
from .serializers import *
from .algorithmn import Backend
from rest_framework.throttling import AnonRateThrottle

from .models import *

from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User
from django.conf import settings

@api_view(['GET'])    #restricted (system data related)
def get_api(request):
	api = {
		'api': settings.API_KEY
		}
	def get_renderers(self):
	    rends = [renderers.JSONRenderer]
	return Response(api)

@api_view(['GET'])    #restricted (system data related)
def Overview(request):
	#print(request.user)
	if request.user.is_authenticated and request.user.is_superuser:
		api_urls = {
			'Clients':'backend/konnect/clients/',
			'Servers':'backend/konnect/servers/',
			'profiles': 'serviceprovider/profiles',
			'authentication': 'authentication/',
			}
		return Response(api_urls)
	else:
		return Response("API Access Denied!")

@api_view(['GET'])   #restricted (system data related)
def apiOverview_servers(request):
	if request.user.is_authenticated:
		api_urls = {
			'List':'dataset/',
			'Motors_SPs_list':'motors_SPs_list/',
			'Motors_SP_detail':'motors_detail/<str:pk>/',
			'Motors_create_SP':'motors_create/',
			'Motors_update_SP_info':'motors_update/<str:pk>/',
			'Motors_delete_SP':'motors_delete/<str:pk>/',
			}
		return Response(api_urls)
	else:
		return Response("API Access Denied!")

@api_view(['GET'])  #restricted (system data related)
def dataset_view(request):
	if request.user.is_authenticated:
		clients = ServiceProvider_Motor.objects.all().order_by('-id')
		serializer = Motor_SerializerCordinates(clients, many=True)

		cords = ServiceProvider_Motor.objects.values_list('cordinate', flat=True)
		
		# dataset = list()
		for i in cords:
			print(i)
		return Response(serializer.data)
	else:
		return Response("API Access Denied!")


#Service provider API CRUD
@api_view(['GET'])  #restricted (system data related)
def MotorsList(request):
	if request.user.is_authenticated:
		motors = ServiceProvider_Motor.objects.all().order_by('-id')
		serializer = ServiceProvider_Motor_Serializer(motors, many=True)
		return Response(serializer.data)
	else:
		return Response("API Access Denied!")

@api_view(['GET'])  #restricted (system data related)
def MotorsDetail(request, pk):
	if request.user.is_authenticated:
		motors = ServiceProvider_Motor.objects.get(id=pk)
		print(motors)
		serializer = ServiceProvider_Motor_Serializer(motors, many=False)
		return Response(serializer.data)
	else:
		return Response("API Access Denied!")

@api_view(['POST'])
def MotorsCreate(request):
	serializer = ServiceProvider_Motor_Serializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def MotorsUpdate(request, pk):
	motor = ServiceProvider_Motor.objects.get(id=pk)
	serializer = ServiceProvider_Motor_Serializer(instance=motor, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['DELETE']) #restricted (system data related)
def MotorsDelete(request, pk):
	if request.user.is_authenticated:
		instanc = ServiceProvider_Motor.objects.get(id=pk)
		instanc.delete()

		return Response('Deleted!')
	else:
		return Response("API Access Denied!")

#Client API CRUD
@api_view(['GET']) #restricted (system data related)
def apiOverview_clients(request):
	if request.user.is_authenticated:
		api_urls = {
			'User dataset':'dataset/',
			'Users List':'users_list/',
			'User detail':'user_detail/<str:pk>/',
			'User create':'user_create/',

			}
		return Response(api_urls)
	else:
		return Response("API Access Denied!")

@api_view(['GET']) #restricted (system data related)
def dataset_users_view(request):
	if request.user.is_authenticated:
		users = Client.objects.all().order_by('-id')
		serializer = UserCordinates_Serializer(users, many=True)

		return Response(serializer.data)
	else:
		return Response("API Access Denied!")

@api_view(['GET']) #restricted (system data related)
def UsersList(request):
	if request.user.is_authenticated:
		users = Client.objects.all().order_by('-id')
		serializer = User_Serializer(users, many=True)
		return Response(serializer.data)
	else:
		return Response("API Access Denied!")

@api_view(['GET']) #restricted (system data related)
def UsersDetail(request, pk):
	if request.user.is_authenticated:
		motors = Client.objects.get(id=pk)
		serializer = User_Serializer(motors, many=False)
		return Response(serializer.data)
	else:
		return Response("API Access Denied!")

@api_view(['POST'])
@throttle_classes([AnonRateThrottle])
def UsersCreate(request):
	serializer = Backend(request)
	return Response(serializer.data)



	

# @api_view(['DELETE'])
# def UsersDelete(request, pk):
# 	instanc = User_Serializer.objects.get(id=pk)
# 	instanc.delete()

# 	return Response('Deleted!')


