from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet
from cars.models import Auto, Categoria, ModeloAuto,Comentario
from api_v1.serializers.cars_serializer  import AutoSerializer
from api_v1.serializers.comentario_serializer import ComentarioSerializer
from api_v1.paginations import MiPaginador
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from api_v1.filters import AutoFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
import csv



class AutoViewSet(ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['nombre', 'precio', 'categoria__nombre']
    filterset_class = AutoFilter  # Cambiado FilterSet_class a filterset_class

    @action(detail=True, methods=['get'], url_path='comentarios')
    def get_comentarios(self, request, pk=None):
        # Intentar obtener el Auto por su ID
        try:
            auto = Auto.objects.get(pk=pk)
        except Auto.DoesNotExist:
            return Response({"error": "Auto no encontrado."}, status=status.HTTP_404_NOT_FOUND)
        
        # Obtener los comentarios asociados al Auto
        comentarios = Comentario.objects.filter(auto=auto)
        serializer = ComentarioSerializer(comentarios, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    @action(detail=True, methods=['delete'], url_path='comentarios/(?P<comentario_id>[^/.]+)')
    def delete_comentario(self, request, pk=None, comentario_id=None):
        # Verificar si el comentario existe
        try:
            comentario = Comentario.objects.get(pk=comentario_id, auto_id=pk)
            comentario.delete()
            return Response({"message": "Comentario eliminado correctamente."}, status=status.HTTP_204_NO_CONTENT)
        except Comentario.DoesNotExist:
            return Response({"error": "Comentario no encontrado."}, status=status.HTTP_404_NOT_FOUND)
 

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT) 


    def create(self, request, *args, **kwargs):
        # Extraemos los datos de la petición
         data = request.data

         # Verificamos que el campo 'categoria' esté presente y sea un nombre válido
         category_name = data.get('categoria', None)
         if not category_name:
             return Response({"error": "El campo 'categoria' es obligatorio y debe contener un nombre válido."}, status=status.HTTP_400_BAD_REQUEST)
        
         # Extraemos o creamos la categoría usando el nombre proporcionado
         category, created = Categoria.objects.get_or_create(nombre=category_name)
        
         # Obtener la instancia de ModeloAuto (si existe)
         modelo_id = data.get('modelo')
         modelo = None
         if modelo_id:
             try:
                 modelo = ModeloAuto.objects.get(id=modelo_id)
             except ModeloAuto.DoesNotExist:
                 return Response({"error": f"El modelo con id {modelo_id} no existe."}, status=status.HTTP_400_BAD_REQUEST)
        
         # Convertimos el valor del campo active de cadena a booleano
         active = data.get('active', False)
         if isinstance(active, str):
             active = active.lower() == "true"
        
         # Creamos el auto
         auto = Auto.objects.create(
             categoria=category,  # Se asegura que se asigne una categoría válida
             precio=data.get('precio', None),
             imagen=data.get('imagen', None),
             pais_fabricacion=data.get('pais_fabricacion', ""),
             combustible=data.get('combustible', ""),
             descripcion=data.get('descripcion', ""),
             active=active,  # Convertido a booleano
             modelo=modelo  # Asignamos la instancia del modelo, si existe
         )
        
         # Serializamos el nuevo objeto creado
         serializer = self.serializer_class(auto)
         return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        


    @action(methods=['get'], detail=False, url_path='download-csv')
    def download_csv(self, request):
        # Definimos el nombre del archivo CSV
        categoria = request.query_params.get('category', None)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="autos.csv"'

        # Escribimos el encabezado del archivo CSV
        writer = csv.writer(response)
        writer.writerow(
            [
                "Modelo", "Descripción", "Precio", "Categoría", "País de Fabricación", "Combustible"
            ]
        )

        # Obtenemos los autos según la categoría filtrada (si se provee)
        autos = self.get_queryset()
        if categoria:
            autos = self.get_queryset().filter(categoria__nombre=categoria)

        # Escribimos los autos en el archivo CSV
        for auto in autos:
            writer.writerow(
                [
                    f'{auto.modelo.marca.nombre} {auto.modelo.nombre}',
                    auto.descripcion,
                    auto.precio,
                    auto.categoria.nombre if auto.categoria else 'No posee',
                    auto.pais_fabricacion or 'Desconocido',
                    auto.conbustible
                ]
            )
        return response

    @action(detail=False, methods=['get'], url_path='download-price-stock-csv')
    def download_price_stock(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="total_price_autos.csv"'

        writer = csv.writer(response)
        writer.writerow(
            [
                "Modelo", "Precio", "Valor Total"
            ]
        )

        # Calculamos el valor total para cada auto (aquí no hay stock, ajustamos)
        for auto in self.get_queryset():
            valor_total = auto.precio  # Si quieres calcular algo adicional, ajústalo aquí
            writer.writerow(
                [
                    f'{auto.modelo.marca.nombre} {auto.modelo.nombre}',
                    auto.precio,
                    valor_total
                ]
            )

        return response

    @action(methods=['get'], detail=False, url_path='latest')
    def last_auto(self, request):
        # Obtenemos el último auto agregado
        last_auto = self.get_queryset().last()
        serializer = self.serializer_class(last_auto)
        return Response(serializer.data)
