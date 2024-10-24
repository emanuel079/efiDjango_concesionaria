# api_v1/serializers/cars_serializer.py
from rest_framework import serializers
from cars.models import Comentario

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = '__all__'
