# 🚌 Transitrack API

## 📖 Descripción
API REST desarrollada con Django REST Framework para administrar rutas de transporte y conductores asignados.

## 🛠️ Tecnologías
- Python 3.12
- Django 6.0.4
- Django REST Framework
- SQLite3

## ⚙️ Instalación y ejecución

1. Clonar el repositorio: `git clone https://github.com/anali-salvador/transitrack_api.git`
2. Crear entorno virtual: `python -m venv myvenv`
3. Activar entorno: `myvenv\Scripts\activate`
4. Instalar dependencias: `pip install django djangorestframework`
5. Aplicar migraciones: `python manage.py migrate`
6. Correr servidor: `python manage.py runserver`

## 🔗 Endpoints

### Conductores
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/conductores/` | Lista conductores |
| POST | `/api/conductores/` | Crea conductor |
| PUT | `/api/conductores/{id}/` | Edita conductor |
| DELETE | `/api/conductores/{id}/` | Elimina conductor |

### Rutas
| Método | Endpoint | Descripción |
|--------|----------|-------------|
| GET | `/api/rutas/` | Lista rutas |
| POST | `/api/rutas/` | Crea ruta |
| PUT | `/api/rutas/{id}/` | Edita ruta |
| DELETE | `/api/rutas/{id}/` | Elimina ruta |
| GET | `/api/rutas/?search=Lima` | Busca rutas |

## 🖼️ Capturas de pantalla

## GET Conductores
![GET Conductores](./docs/01-get-conductores.png)

## POST Conductor
![POST Conductor](./docs/02-post-conductor.png)

## PUT Conductor
![PUT Conductor](./docs/03-put-conductor.png)

## DELETE Conductor
![DELETE Conductor](./docs/04-delete-conductor.png)

## GET Rutas
![GET Rutas](./docs/05-get-rutas.png)

## POST Ruta
![POST Ruta](./docs/06-post-ruta.png)

## PUT Ruta
![PUT Ruta](./docs/07-put-ruta.png)

## DELETE Ruta
![DELETE Ruta](./docs/08-delete-ruta.png)

## Búsqueda de Rutas
![Búsqueda](./docs/09-search-ruta.png)

## Relación Ruta con Conductor
![Relación](./docs/10-relacion.png)

## 🙌 Autor
**Anali Salvador Advincula** - Estudiante de Tecsup