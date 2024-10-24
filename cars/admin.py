from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Marca,
    ModeloAuto,
    Categoria,
    Auto,
    Cliente,
    Comentario,
    Venta,
    Empleado,
    Proveedor,
    Servicio,
    Cita,
    Accesorio
)

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    ordering = ('modelo', 'precio')
    search_fields = ('precio', 'modelo__nombre', 'categoria__nombre',)
    list_filter = ('categoria', 'modelo',)
    empty_value_display = "No hay datos para este campo"
    
    list_display = (
        'modelo',
        'precio',
        'descripcion',
        'categoria',
        'thumbnail',  # Añadimos esta línea
    )

    fieldsets = [
        (
            "Info del Auto",
            {
                "fields" : ["modelo", "precio", "categoria", "pais_fabricacion", "conbustible"],
            }
        ),
        (
            "Info Extra",
            {
                "classes":["collapse"],
                "fields" : ["imagen", "descripcion"]
            }
        )
    ]

    def thumbnail(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="width: 45px; height:45px;" />'.format(obj.imagen.url))
        return ""
    thumbnail.short_description = 'Imagen'

# Los demás modelos quedan igual
@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
    )

@admin.register(ModeloAuto)
class ModeloAutoAdmin(admin.ModelAdmin):
    list_display = (
        'marca', 'nombre', 'anio',
    )

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = (
        'nombre', 'puertas',
    )

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'telefono', 'direccion',
    )

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = (
        'auto', 'usuario', 'comentario', 'fecha',
    )

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = (
        'auto', 'cliente', 'fecha', 'precio_final',
    )

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'puesto',
    )

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = (
        'nombre', 'telefono', 'direccion',
    )

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = (
        'nombre', 'descripcion', 'precio',
    )

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = (
        'cliente', 'servicio', 'fecha', 'descripcion',
    )

@admin.register(Accesorio)
class AccesorioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio',)
