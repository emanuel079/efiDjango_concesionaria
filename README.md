# Sistema de Gestión de Productos y Categorías

Este proyecto es una aplicación web integral diseñada para la gestión eficiente de una concesionaria de autos. La plataforma permite a los usuarios llevar a cabo diversas operaciones relacionadas con la administración de vehículos, incluyendo la creación, lectura, actualización y eliminación (CRUD) de autos, marcas, modelos, y clientes. Además, ofrece funcionalidades para gestionar categorías, comentarios de los usuarios y la relación con proveedores. 

El sistema está construido para diferenciar entre usuarios con diferentes roles, como staff y clientes, proporcionando niveles de acceso adecuados según las necesidades de la concesionaria. Los usuarios con rol de staff pueden administrar los vehículos y acceder a funcionalidades avanzadas, mientras que los clientes pueden interactuar con la plataforma, dejando comentarios y visualizando la información de los autos disponibles.

Esta solución busca mejorar la eficiencia operativa de la concesionaria, facilitar la interacción con los clientes y asegurar un manejo organizado de toda la información relevante para el negocio.



## Tecnologías Utilizadas

- HTML
- CSS
- Python
- Django
- Bootstrap 

## Instalación

1. Crea un entorno virtual para el proyecto (recomendado) y actívalo:

    - Para crear un entorno virtual con Python 3:
    
      ```bash
      python3 -m venv nombre_del_entorno
      ```

    - Activa el entorno virtual:
    
      - En Windows:
        ```bash
        nombre_del_entorno\Scripts\activate
        ```
        
      - En macOS y Linux:
        ```bash
        source nombre_del_entorno/bin/activate
        ```
        
2. Crea una nueva carpeta para clonar el repositorio.

    ```bash
    mkdir nombre_de_la_carpeta
    ```

3. Accede a la nueva carpeta:

   ```bash
    cd nombre_de_la_carpeta
    ```

4. Clona este repositorio en tu máquina local usando el siguiente comando:

    ```bash
    git clone git@github.com:emanuel079/proyect_django.git
    ```

5. Navega hasta el directorio del proyecto:

    ```bash
    cd proyect_django
    ```

6. Instala las dependencias del proyecto:

    ```bash
    pip install -r requirements.txt
    ```

7. Ejecuta las migraciones para crear las tablas en la base de datos:

    ```bash
    python manage.py migrate
    ```

8. Inicia el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

9. Abre un navegador web y accede a `http://localhost:8000` para comenzar a utilizar la aplicación.


## Funcionalidades

**Gestión de Categorías**

- Agregar Categorías: Los usuarios pueden agregar nuevas categorías para organizar los productos.
- Actualizar Categorías: Los usuarios pueden modificar el nombre de las categorías existentes.
- Eliminar Categorías: Los usuarios pueden eliminar categorías que ya no sean necesarias.

**Gestión de Productos** 

- Agregar Productos: Los usuarios pueden agregar nuevos productos asociados a una categoría específica.
- Actualizar Productos: Los usuarios pueden modificar la información de los productos, como nombre, descripción, precio y stock.
- Eliminar Productos: Los usuarios pueden eliminar productos que ya no estén en venta o que sean obsoletos.
- Visualizar Detalles de Producto: Los usuarios pueden ver información detallada de cada producto, incluyendo su categoría y características.

## Autor ✒️

- Franco Emanuel Benitez - [@emanuel079](https://github.com/emanuel079)
- Cintia Gisele Rojo- [@cinrojo](https://github.com/cinrojo)
- Lautaro Palacios - [@Lautaro-Palacios](https://github.com/Lautaro-Palacios)
  
