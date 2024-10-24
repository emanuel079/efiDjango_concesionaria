# api_v1/views/user.py
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from api_v1.serializers.user_serializer import UserSerializer
from rest_framework.response import Response  # Asegúrate de importar Response
from rest_framework import status



class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def create(self, request, *args, **kwargs):
        data = request.data
        
        # Extraer los datos necesarios para crear el usuario
        username = data.get('username')
        password = data.get('password')
        first_name = data.get('first_name', '')
        last_name = data.get('last_name', '')
        email = data.get('email', '')
        
        # Crear el usuario
        user = User.objects.create_user(
            username=username, 
            password=password, 
            first_name=first_name, 
            last_name=last_name, 
            email=email
        )
        
        # Serializar el usuario creado
        serializer = self.serializer_class(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
