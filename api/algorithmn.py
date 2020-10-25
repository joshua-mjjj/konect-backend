from django.shortcuts import render
from django.http import JsonResponse
from math import sqrt, radians, cos, sin, asin, degrees, atan2
import numpy as np


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import (
ServiceProvider_Motor_Serializer,
Motor_SerializerCordinates,
User_Serializer,
UserCordinates_Serializer
)

from .models import ServiceProvider_Motor, Client


def Backend(request):
	serializer = User_Serializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	
	# for i in dataset:
	# 	print(i)

	def validate_point(p):
		lat, lon, prmry = p
		assert -90<=lat<=90
		assert -180<=lon<=180

	def great_circle_distance(point1, point2):
		lat1, lon1, primary1 = point1
		lat2, lon2, primary2 = point2
		# print(primary1)
		# print(primary2)

		for p in [point1, point2]:
			validate_point(p)

		lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

		dlon = lon2 - lon1
		dlat = lat2 - lat1
		R = 6371 #km -- earth's radius

		a = sin(dlat/2)**2 + cos(lat1)*cos(lat2) * sin(dlon/2)**2
		c = 2 * asin(sqrt(a))
		d = R*c
		#return dlon, dlat
		return d

	#function for getting the closest  neigbours
	def get_neighbours(train, test_row, num_neighbours):
		distances = list()
		for train_row in train:
			dist = great_circle_distance(test_row, train_row)
			distances.append((train_row, dist))
		distances.sort(key=lambda tup: tup[1])
		neighbours = list()
		for i in range(num_neighbours):
			neighbours.append(distances[i][0])
		return neighbours

	#print(serializer.data)
	case_cordinate = serializer.data['cordinate']
	lat = serializer.data['lat']
	lon = serializer.data['lon']
	vague_id = 0
	cordinate = list()
	cordinate.append(lat)
	cordinate.append(lon)
	cordinate.append(vague_id)
	
	neighbours = serializer.data['neighbours']
	#print(neighbours)

	clients = ServiceProvider_Motor.objects.all().order_by('-id')
	dataset = ServiceProvider_Motor.objects.values_list('lat', 'lon', 'id')

	neighbours = get_neighbours(dataset,cordinate, neighbours)
	print(neighbours)
	result_serializer = list()
	for neighbour in neighbours:
		pk = neighbour[2]
		result = ServiceProvider_Motor.objects.get(id=pk)
		serializer = ServiceProvider_Motor_Serializer(result, many=False)

		result_serializer.append(serializer.data)
		
	print(result_serializer)

	return Response(result_serializer)
