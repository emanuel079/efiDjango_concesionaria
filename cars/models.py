from django.db import models
from django.contrib.auth.models import User
from cars.managers import AutoQuerySet
from django.utils.translation import gettext_lazy as _

class Marca(models.Model):
    nombre = models.CharField(max_length=100, verbose_name=_("Nombre"))

    def __str__(self):
        return self.nombre

class ModeloAuto(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name=_("Marca"))
    nombre = models.CharField(max_length=100, verbose_name=_("Nombre"))
    anio = models.CharField(max_length=4, null=False, default="2020", verbose_name=_("Año"))

    def __str__(self):
        return f'{self.marca.nombre} {self.nombre}'

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name=_("Nombre"))
    puertas = models.IntegerField(null=False, default=4, verbose_name=_("Puertas"))

    def __str__(self):
        return self.nombre

class Auto(models.Model):
    modelo = models.ForeignKey(ModeloAuto, on_delete=models.CASCADE, verbose_name=_("Modelo"))
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name=_("Categoría"))
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Precio"))
    imagen = models.ImageField(upload_to='autos/', verbose_name=_("Imagen"))
    pais_fabricacion = models.CharField(max_length=100, null=True, blank=True, verbose_name=_("País de fabricación"))
    combustible = models.CharField(max_length=50, default='Gasolina', verbose_name=_("Combustible"))
    descripcion = models.TextField(verbose_name=_("Descripción"))
    active = models.BooleanField(default=True, verbose_name=_("Activo"))

    objects = AutoQuerySet.as_manager()

    def __str__(self):
        return f'{self.modelo.marca.nombre} {self.modelo.nombre}'

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("Usuario"))
    telefono = models.CharField(max_length=15, verbose_name=_("Teléfono"))
    direccion = models.CharField(max_length=255, verbose_name=_("Dirección"))
    is_staff_user = models.BooleanField(default=False, verbose_name=_("Es usuario staff"))

    def __str__(self):
        return self.user.username

class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Usuario"))
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, verbose_name=_("Auto"))
    comentario = models.TextField(verbose_name=_("Comentario"))
    fecha = models.DateTimeField(auto_now_add=True, verbose_name=_("Fecha"))

    def __str__(self):
        return self.comentario[:50]

class Accesorio(models.Model):
    nombre = models.CharField(max_length=100, verbose_name=_("Nombre"))
    descripcion = models.TextField(verbose_name=_("Descripción"))
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Precio"))
    autos = models.ManyToManyField(Auto, related_name='accesorios', verbose_name=_("Autos"))
    imagen = models.ImageField(upload_to='accesorios/', null=True, blank=True, verbose_name=_("Imagen"))

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, verbose_name=_("Auto"))
    accesorio = models.ForeignKey(Accesorio, on_delete=models.CASCADE, default=1, verbose_name=_("Accesorio"))
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name=_("Cliente"))
    fecha = models.DateTimeField(auto_now_add=True, verbose_name=_("Fecha"))
    precio_final = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Precio final"))

    def __str__(self):
        return f'{self.cliente.user.username} - {self.auto.modelo.nombre}'

class Empleado(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("Usuario"))
    puesto = models.CharField(max_length=100, verbose_name=_("Puesto"))
    imagen = models.ImageField(upload_to='empleados/', null=True, blank=True, verbose_name=_("Imagen"))

    def __str__(self):
        return self.user.username

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100, verbose_name=_("Nombre"))
    telefono = models.CharField(max_length=15, verbose_name=_("Teléfono"))
    direccion = models.CharField(max_length=255, verbose_name=_("Dirección"))
    autos = models.ManyToManyField(Auto, verbose_name=_("Autos"))

    def __str__(self):
        return self.nombre

class Servicio(models.Model):
    nombre = models.CharField(max_length=100, verbose_name=_("Nombre"))
    descripcion = models.TextField(verbose_name=_("Descripción"))
    precio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name=_("Precio"))

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, verbose_name=_("Cliente"))
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE, verbose_name=_("Servicio"))
    fecha = models.DateTimeField(verbose_name=_("Fecha"))
    descripcion = models.TextField(verbose_name=_("Descripción"))

    def __str__(self):
        return f'{self.cliente.user.username} - {self.servicio.nombre}'
