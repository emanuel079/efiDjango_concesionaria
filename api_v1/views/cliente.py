# api_v1/views/cliente.py
from django.contrib.auth.models import User
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from cars.models import Cliente
from api_v1.serializers.cliente_serializer import ClienteSerializer
from api_v1.serializers.user_serializer import UserSerializer  # Importa el serializador de usuario

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post', 'get'], url_path='crear-cliente')
    def crear_cliente(self, request, pk=None):
        # Obtener el usuario basado en `pk` (user_id)
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": "Usuario no encontrado."}, status=status.HTTP_404_NOT_FOUND)

        # Si es una solicitud GET, devuelve detalles del usuario
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response({"user_details": user_serializer.data}, status=status.HTTP_200_OK)

        # Si es una solicitud POST, crear el cliente
        if request.method == 'POST':
            if not request.user.is_staff:
                return Response({"error": "No tienes permiso para crear un cliente."}, status=status.HTTP_403_FORBIDDEN)
            
            # Verificar si ya existe un cliente asociado al usuario
            if Cliente.objects.filter(user=user).exists():
                return Response({"error": "Este usuario ya tiene un cliente asociado."}, status=status.HTTP_400_BAD_REQUEST)

            # Crear el cliente con los datos proporcionados
            data = request.data
            serializer = ClienteSerializer(data=data)
            if serializer.is_valid():
                serializer.save(user=user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
