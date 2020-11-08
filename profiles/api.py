from profiles.models import serviceProvider
from rest_framework.response import Response
from rest_framework import viewsets, permissions
from .serializers import ProfileSerializer
import os
import shutil
from django.conf import settings

class ProfileViewSet(viewsets.ModelViewSet):
	#queryset = serviceProvider.objects.all()
	
	permission_classes = [permissions.IsAuthenticated, ]
	serializer_class = ProfileSerializer
	def get_queryset(self):
		if self.request.user.is_superuser and self.request.user.id == 1:
			queryset = serviceProvider.objects.all()
			return queryset
		else:
			return  self.request.user.profiles.all()

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)
		#saving a lead to its owner

	def destroy(self, request, *args, **kwargs):
		instance = self.get_object()
		path_to_image = str(instance.profile_picture)
		self.perform_destroy(instance)
		os.remove(os.path.join(settings.MEDIA_ROOT, path_to_image)) # deleteiing images so we don't croud the server.
		return Response('Profile Deleted!')

	def perform_update(self, serializer):
		location = 'profile_pictures'
		path_to_image = os.path.join(location, str(self.request.user))
		shutil.rmtree(path_to_image)                                   # deleteiing images so we don't croud the server.
		serializer.save(owner=self.request.user)
		
		return Response('Profile Updated!')