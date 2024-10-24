# api_v1/serializers/cars_serializer.py
from rest_framework import serializers
from cars.models import Marca, ModeloAuto

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('id', 'nombre')  # Asegúrate de incluir los campos necesarios

class ModeloAutoSerializer(serializers.ModelSerializer):
    marca = MarcaSerializer()

    class Meta:
        model = ModeloAuto
        fields = '__all__'

    def update(self, instance, validated_data):
        # Obtiene los datos de la marca
        marca_data = validated_data.pop('marca', None)
        
        if marca_data:
            # Busca o crea la marca
            marca, _ = Marca.objects.get_or_create(**marca_data)
            instance.marca = marca

        # Actualiza los campos del modelo ModeloAuto
        instance.nombre = validated_data.get('nombre', instance.nombre)
        instance.anio = validated_data.get('anio', instance.anio)

        # Guarda los cambios
        instance.save()
        return instance
