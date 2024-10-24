import factory
from cars.models import Auto, Categoria,ModeloAuto
from .factories import CategoriaFactory, ModeloAutoFactory

class AutoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Auto

    modelo = factory.SubFactory(ModeloAutoFactory)
    categoria = factory.SubFactory(CategoriaFactory)
    precio = factory.Faker('pydecimal', left_digits=5, right_digits=2, positive=True)
    imagen = factory.django.ImageField(filename='auto.jpg')
    pais_fabricacion = factory.Faker('country')
    conbustible = factory.Faker('word')
    descripcion = factory.Faker('text')
    active = factory.Faker('boolean')

class ModeloAutoFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ModeloAuto

    marca = factory.SubFactory(MarcaFactory)
    nombre = factory.Faker('word')
    anio = factory.Faker('year')

class CategoriaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Categoria

    nombre = factory.Faker('word')
    puertas = factory.Faker('random_int', min=2, max=5)
