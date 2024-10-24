from django.urls import path

from users.views import StaffView
from cars.views.auto_view import AutoListView, AutoDetailView, AutoCreateView, AutoUpdateView, AutoDeleteView
from cars.views.accesorio_view import AccesorioListView, AccesorioDetailView, AccesorioCreateView, AccesorioUpdateView, AccesorioDeleteView
from cars.views.category_view import CategoriaListView, CategoriaDetailView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView
from cars.views.cita_view import CitaListView, CitaDetailView, CitaCreateView, CitaUpdateView, CitaDeleteView
from cars.views.empleado_view import EmpleadoListView, EmpleadoDetailView, EmpleadoCreateView, EmpleadoUpdateView, EmpleadoDeleteView
from cars.views.marca_view import MarcaListView, MarcaDetailView, MarcaCreateView, MarcaUpdateView, MarcaDeleteView
from cars.views.modelo_auto_view import ModeloAutoListView, ModeloAutoDetailView, ModeloAutoCreateView, ModeloAutoUpdateView, ModeloAutoDeleteView
from cars.views.proveedor_view import ProveedorListView, ProveedorDetailView, ProveedorCreateView, ProveedorUpdateView, ProveedorDeleteView
from cars.views.servicio_view import ServicioListView, ServicioDetailView, ServicioCreateView, ServicioUpdateView, ServicioDeleteView
from cars.views.venta_view import VentaListView, VentaDetailView, VentaCreateView, VentaUpdateView, VentaDeleteView
from cars.views.comentario_view import (
    ComentariosPorAutoView,
    ComentarioCreateView,
    ComentarioDetailView,
    ComentarioUpdateView,
    ComentarioDeleteView
)
from cars.views.cliente_view import (
    ClienteListView,
    ClienteDetailView,
    ClienteCreateView,
    ClienteUpdateView,
    ClienteDeleteView
)

urlpatterns = [

    path('comentarios/auto/<int:auto_pk>/', ComentariosPorAutoView.as_view(), name='comentarios_por_auto'),
    path('comentarios/nuevo/<int:auto_pk>/', ComentarioCreateView.as_view(), name='comentario_create_auto'),
    path('comentarios/<int:pk>/', ComentarioDetailView.as_view(), name='comentario_detail'),
    path('comentarios/<int:pk>/editar/', ComentarioUpdateView.as_view(), name='comentario_update'),
    path('comentarios/<int:pk>/eliminar/', ComentarioDeleteView.as_view(), name='comentario_delete'),

    path('ventas/', VentaListView.as_view(), name='venta_list'),
    path('ventas/<int:pk>/', VentaDetailView.as_view(), name='venta_detail'),
    path('ventas/nueva/', VentaCreateView.as_view(), name='venta_create'),
    path('ventas/<int:pk>/editar/', VentaUpdateView.as_view(), name='venta_update'),
    path('ventas/<int:pk>/eliminar/', VentaDeleteView.as_view(), name='venta_delete'),

    path('servicios/', ServicioListView.as_view(), name='servicio_list'),
    path('servicios/<int:pk>/', ServicioDetailView.as_view(), name='servicio_detail'),
    path('servicios/nuevo/', ServicioCreateView.as_view(), name='servicio_create'),
    path('servicios/<int:pk>/editar/', ServicioUpdateView.as_view(), name='servicio_update'),
    path('servicios/<int:pk>/eliminar/', ServicioDeleteView.as_view(), name='servicio_delete'),

    path('proveedores/', ProveedorListView.as_view(), name='proveedores_list'),
    path('proveedores/<int:pk>/', ProveedorDetailView.as_view(), name='proveedores_detail'),
    path('proveedores/nuevo/', ProveedorCreateView.as_view(), name='proveedores_create'),
    path('proveedores/<int:pk>/editar/', ProveedorUpdateView.as_view(), name='proveedores_update'),
    path('proveedores/<int:pk>/eliminar/', ProveedorDeleteView.as_view(), name='proveedores_delete'),

    path('modelos/', ModeloAutoListView.as_view(), name='modelo_auto_list'),
    path('modelos/<int:pk>/', ModeloAutoDetailView.as_view(), name='modelo_auto_detail'),
    path('modelos/nuevo/', ModeloAutoCreateView.as_view(), name='modelo_auto_create'),
    path('modelos/<int:pk>/editar/', ModeloAutoUpdateView.as_view(), name='modelo_auto_update'),
    path('modelos/<int:pk>/eliminar/', ModeloAutoDeleteView.as_view(), name='modelo_auto_delete'),

    path('marcas/', MarcaListView.as_view(), name='marca_list'),
    path('marcas/<int:pk>/', MarcaDetailView.as_view(), name='marca_detail'),
    path('marcas/nueva/', MarcaCreateView.as_view(), name='marca_create'),
    path('marcas/<int:pk>/editar/', MarcaUpdateView.as_view(), name='marca_update'),

    path('empleados/', EmpleadoListView.as_view(), name='empleados_list'),
    path('empleados/<int:id>/', EmpleadoDetailView.as_view(), name='empleados_detail'),
    path('empleados/nuevo/', EmpleadoCreateView.as_view(), name='empleados_create'),
    path('empleados/<int:id>/editar/', EmpleadoUpdateView.as_view(), name='empleados_update'),
    path('empleados/<int:id>/eliminar/', EmpleadoDeleteView.as_view(), name='empleados_delete'), 


    path('citas/', CitaListView.as_view(), name='cita_list'),
    path('citas/<int:id>/', CitaDetailView.as_view(), name='cita_detail'),
    path('citas/nueva/', CitaCreateView.as_view(), name='cita_create'),
    path('citas/<int:id>/editar/', CitaUpdateView.as_view(), name='cita_update'),
    path('citas/<int:id>/eliminar/', CitaDeleteView.as_view(), name='cita_delete'),

    path('categorias/', CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/<int:pk>/', CategoriaDetailView.as_view(), name='categoria_detail'),
    path('categorias/nuevo/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/<int:pk>/editar/', CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categorias/<int:pk>/eliminar/', CategoriaDeleteView.as_view(), name='categoria_delete'),


    path('accesorios/', AccesorioListView.as_view(), name='accesorios_list'),
    path('accesorios/<int:pk>/', AccesorioDetailView.as_view(), name='accesorios_detail'),
    path('accesorios/nuevo/', AccesorioCreateView.as_view(), name='accesorios_create'),
    path('accesorios/<int:pk>/editar/', AccesorioUpdateView.as_view(), name='accesorios_update'),
    path('accesorios/<int:pk>/eliminar/', AccesorioDeleteView.as_view(), name='accesorios_delete'),

    
    path('clientes/', ClienteListView.as_view(), name='cliente_list'),
    path('clientes/<int:id>/', ClienteDetailView.as_view(), name='cliente_detail'),
    path('clientes/create/', ClienteCreateView.as_view(), name='cliente_create'),
    path('clientes/update/<int:id>/', ClienteUpdateView.as_view(), name='cliente_update'),
    path('clientes/delete/<int:id>/', ClienteDeleteView.as_view(), name='cliente_delete'),


    path('autos/', AutoListView.as_view(), name='auto_list'),
    path('autos/nuevo/', AutoCreateView.as_view(), name='auto_create'),
    path('autos/<int:pk>/', AutoDetailView.as_view(), name='auto_detail'),
    path('autos/<int:pk>/editar/', AutoUpdateView.as_view(), name='auto_update'),
    path('autos/<int:pk>/eliminar/', AutoDeleteView.as_view(), name='auto_delete'),
]
