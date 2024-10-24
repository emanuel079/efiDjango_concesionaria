from rest_framework import serializers
from cars.models import Auto, Categoria


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('nombre', 'pk')


class AutoSerializer(serializers.ModelSerializer):
    categoria = CategorySerializer()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Auto
        fields = '__all__'

    def get_description(self, obj):
        if obj.descripcion is None:
            return "No posee descripción"
        return obj.descripcion

    def update(self, instance, validated_data):
        # Obtiene los datos de la categoría
        category_data = validated_data.pop('categoria', None)  # Usar 'categoria' en lugar de 'category'
        
        if category_data:
            # Busca o crea la categoría
            categoria, _ = Categoria.objects.get_or_create(**category_data)
            instance.categoria = categoria  # Usar 'categoria' en lugar de 'category'

        # Actualiza los campos del modelo Auto
        instance.name = validated_data.get('nombre', instance.name)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.price = validated_data.get('precio', instance.price)
        instance.active = validated_data.get('active', instance.active)
        

        # Guarda los cambios
        instance.save()
        return instance
