# Django Database Integration & Architecture

Este repositorio demuestra la implementación de un backend robusto utilizando **Django**, enfocado en la transición de un sistema de datos estáticos a una arquitectura de persistencia dinámica. El proyecto se centra en la configuración, conexión y gestión de una base de datos externa PostgreSQL, asegurando la integridad de la información mediante el ORM de Django.

## 🚀 Objetivos y Capacidades Técnicas

* **Conectividad de Base de Datos:** Configuración avanzada de motores de bases de datos relacionales en entornos Django.
* **Modelado de Datos (ORM):** Creación de esquemas relacionales eficientes, definiendo tipos de campos, validaciones y relaciones entre entidades.
* **Persistencia Dinámica:** Implementación de la capa de modelos para permitir que la aplicación realice operaciones CRUD completas de forma persistente.
* **Gestión de Entornos:** Configuración segura de parámetros de conexión mediante mejores prácticas de desarrollo.

## 🛠️ Stack Tecnológico

* **Lenguaje:** Python 3.x
* **Framework:** Django 4.x / 5.x
* **Base de Datos:** PostgreSQL.
* **Control de Versiones de DB:** Django Migrations

## ⚙️ Resolución del Desafío Técnico

El desarrollo se centró en establecer un puente de comunicación eficiente entre la lógica de negocio y el almacenamiento:

1. **Configuración de Engine:** Se integraron los drivers necesarios (como `psycopg2` para Postgres) para permitir la comunicación fluida entre Python y el motor de base de datos.
2. **Abstracción de Datos:** Se utilizaron los Modelos de Django para abstraer la complejidad de SQL, permitiendo una gestión de datos más segura y orientada a objetos.
3. **Sincronización de Esquemas:** Aplicación de migraciones para reflejar los cambios en los modelos directamente en la estructura de las tablas de la base de datos, garantizando la consistencia del sistema.

## 📌 Configuración Inicial

Para replicar este entorno localmente, se deben seguir estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/longaresf/django-db-integration.git](https://github.com/longaresf/django-db-integration.git)
    ````
2. Instalar dependencias:
  Bash
  pip install -r requirements.txt

3. Configurar la base de datos:
Asegúrate de tener instalado el motor de base de datos y configurar las credenciales en el archivo settings.py (o en un archivo .env si se implementó).

4. Ejecutar migraciones:
  Bash
  python manage.py makemigrations
  python manage.py migrate

5. Correr el servidor:
  Bash
  python manage.py runserver

✒️ Autor

    Francisco Longares - Desarrollador Backend Python - longaresf

    Este proyecto forma parte del desarrollo de competencias en arquitectura de datos dentro del programa Full Stack Python de Desafío Latam.
