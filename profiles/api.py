from profiles.models import serviceProvider
from rest_framework import viewsets, permissions
from .serializers import ProfileSerializer

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