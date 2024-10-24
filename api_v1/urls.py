from rest_framework.routers import DefaultRouter

from api_v1.views.cars import AutoViewSet
from api_v1.views.marca import MarcaViewSet
from api_v1.views.user import UserViewSet
from api_v1.views.cliente import ClienteViewSet


routers = DefaultRouter()
routers.register(r'cars', AutoViewSet, 'cars')
routers.register(r'marcas', MarcaViewSet, 'marca')
routers.register(r'usuarios', UserViewSet, 'usuarios')
routers.register(r'clientes', ClienteViewSet, 'clientes')

urlpatterns = routers.urls