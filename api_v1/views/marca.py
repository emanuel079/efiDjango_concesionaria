from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from cars.models import Marca
from api_v1.serializers.marca_serializer import MarcaSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from django.http import HttpResponse
import csv

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer
    filter_backends = [SearchFilter]
    search_fields = ['nombre']

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def create(self, request, *args, **kwargs):
        # Extraemos los datos de la petición
        data = request.data

        # Verificamos que el campo 'nombre' de la marca esté presente
        marca_nombre = data.get('nombre', None)
        if not marca_nombre:
            return Response({"error": "El campo 'nombre' es obligatorio y debe contener un nombre válido."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Extraemos o creamos la marca usando el nombre proporcionado
        marca, created = Marca.objects.get_or_create(nombre=marca_nombre)

        # Serializamos el nuevo objeto creado
        serializer = self.serializer_class(marca)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=['get'], detail=False, url_path='download-csv')
    def download_csv(self, request):
        # Definimos el nombre del archivo CSV
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="marcas.csv"'

        # Escribimos el encabezado del archivo CSV
        writer = csv.writer(response)
        writer.writerow(["ID", "Nombre"])

        # Obtenemos todas las marcas y las escribimos en el archivo CSV
        marcas = self.get_queryset()
        for marca in marcas:
            writer.writerow([marca.id, marca.nombre])

        return response

    @action(detail=False, methods=['get'], url_path='latest')
    def last_marca(self, request):
        # Obtenemos la última marca agregada
        last_marca = self.get_queryset().last()
        serializer = self.serializer_class(last_marca)
        return Response(serializer.data)
