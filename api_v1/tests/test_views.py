import pytest
from django.urls import reverse
from rest_framework import status 
from rest_framework.test import APIClient
from cars.models import Auto
from cars.factories import AutoFactory, CategoriaFactory, ModeloAutoFactory

# Tests para las vistas del modelo Auto

# Test básico de ejemplo
def test_first_test():
    assert 3 == 3

# Test para listar autos
@pytest.mark.django_db
def test_list_autos(client: APIClient):
    # Arrange (Preparar)
    auto_1 = AutoFactory()
    auto_2 = AutoFactory()

    # Act (Acción)
    url = reverse('auto-list')  # Ajusta el nombre de la ruta según tu proyecto
    response = client.get(path=url)

    # Assert (Afirmación)
    expected_result = {
        'count': 2,
        'next': None,
        'previous': None,
        'results': [
            {
                "id": auto_1.id,
                "modelo": {
                    "nombre": auto_1.modelo.nombre,
                    "pk": auto_1.modelo.pk
                },
                "categoria": {
                    "nombre": auto_1.categoria.nombre,
                    "pk": auto_1.categoria.pk
                },
                "precio": f"{auto_1.precio}",
                "pais_fabricacion": auto_1.pais_fabricacion,
                "conbustible": auto_1.conbustible,
                "descripcion": auto_1.descripcion,
                "active": auto_1.active,
            },
            {
                "id": auto_2.id,
                "modelo": {
                    "nombre": auto_2.modelo.nombre,
                    "pk": auto_2.modelo.pk
                },
                "categoria": {
                    "nombre": auto_2.categoria.nombre,
                    "pk": auto_2.categoria.pk
                },
                "precio": f"{auto_2.precio}",
                "pais_fabricacion": auto_2.pais_fabricacion,
                "conbustible": auto_2.conbustible,
                "descripcion": auto_2.descripcion,
                "active": auto_2.active,
            }
        ]
    }
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_result

# Test para el detalle de un auto
@pytest.mark.django_db
def test_detail_auto(client: APIClient):
    # Arrange
    auto = AutoFactory()

    # Act
    url = reverse('auto-detail', args=(auto.pk,))  # Ajusta el nombre de la ruta según tu proyecto
    response = client.get(path=url)

    # Assert
    expected_result = dict(
        modelo=dict(
            nombre=auto.modelo.nombre,
            pk=auto.modelo.pk
        ),
        categoria=dict(
            nombre=auto.categoria.nombre,
            pk=auto.categoria.pk
        ),
        precio=f"{auto.precio}",
        pais_fabricacion=auto.pais_fabricacion,
        conbustible=auto.conbustible,
        descripcion=auto.descripcion,
        active=auto.active,
        id=auto.id
    )
    
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == expected_result

# Test para eliminar un auto
@pytest.mark.django_db
def test_delete_auto(client: APIClient):
    # Arrange
    auto = AutoFactory()

    # Act
    url = reverse('auto-detail', args=(auto.pk,))  # Ajusta el nombre de la ruta según tu proyecto
    response = client.delete(path=url)

    # Assert
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Auto.objects.filter(pk=auto.pk).exists()

# Test para crear un auto
@pytest.mark.django_db
def test_create_auto(client: APIClient):
    # Arrange
    categoria = CategoriaFactory()
    modelo = ModeloAutoFactory()
    
    data = {
        "categoria": {
            "nombre": categoria.nombre,
            "pk": categoria.pk
        },
        "modelo": {
            "nombre": modelo.nombre,
            "pk": modelo.pk
        },
        "precio": "100000",
        "pais_fabricacion": "Argentina",
        "conbustible": "Gasolina",
        "descripcion": "Auto de prueba",
        "active": True
    }

    # Act
    url = reverse('auto-list')  # Ajusta el nombre de la ruta según tu proyecto
    response = client.post(
        path=url,
        data=data,
        content_type='application/json'
    )

    # Assert
    assert response.status_code == status.HTTP_201_CREATED
    assert Auto.objects.count() == 1
