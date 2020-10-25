from rest_framework import serializers
from profiles.models import serviceProvider 

# serviceProvider Serializer
class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = serviceProvider 
    fields = '__all__'