from django.db import models
from django.contrib.auth.models import User

class Marca(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class ModeloAuto(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    anio = models.CharField(max_length=4, null=False, default="2020")

    def __str__(self):
        return f'{self.marca.nombre} {self.nombre}'

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    puertas = models.IntegerField(null=False, default=4)

    def __str__(self):
        return self.nombre

class Auto(models.Model):
    modelo = models.ForeignKey(ModeloAuto, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='autos/')
    pais_fabricacion = models.CharField(max_length=100, null=True, blank=True)
    conbustible = models.CharField(max_length=50, default='Gasolina')
    descripcion = models.TextField()

    def __str__(self):
        return f'{self.modelo.marca.nombre} {self.modelo.nombre}'


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    is_staff_user = models.BooleanField(default=False)  # Determina si el usuario es staff

    def __str__(self):
        return self.user.username

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comentario[:50]

class Accesorio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    autos = models.ManyToManyField(Auto, related_name='accesorios')
    imagen = models.ImageField(upload_to='accesorios/', null=True, blank=True)

    def _str_(self):
        return self.nombre
        
class Venta(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    accesorio = models.ForeignKey(Accesorio, on_delete=models.CASCADE, default=1)  # Valor predeterminado
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    precio_final = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.cliente.user.username} - {self.auto.modelo.nombre}'

class Empleado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    puesto = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='empleados/', null=True, blank=True)

    def __str__(self):
        return self.user.username 

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    direccion = models.CharField(max_length=255)
    autos = models.ManyToManyField(Auto)

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.nombre

from django.db import models

class Cita(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    descripcion = models.TextField()

    def __str__(self):
        return f'{self.cliente.user.username} - {self.servicio.nombre}'
