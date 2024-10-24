# api_v1/serializers/cliente_serializer.py
from rest_framework import serializers
from cars.models import Cliente
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

class ClienteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Incluye el usuario relacionado en la respuesta

    class Meta:
        model = Cliente
        fields = ('user', 'telefono', 'direccion')
