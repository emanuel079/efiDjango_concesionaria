from django.urls import path
from django.http import HttpResponse
from users.views import RegisterView
from django.contrib.auth import views as auth_views

from home.views import (
    index_view,
    LogoutView,
    LoginView,
     # Añadir esta línea al final de la lista de URLs de la app home.py.
)

urlpatterns = [
    path(route='',view=index_view, name='index'),
    path(route='login/', view=LoginView.as_view(), name='login'),
    path(route='logout/', view=LogoutView.as_view(), name='logout'),
    
    
]