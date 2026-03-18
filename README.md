# 3.7.-Resolver-problema-mediante-una-API
<p align="center">
  <img width="100%" src="https://raw.githubusercontent.com/Platane/snk/output/github-contribution-grid-snake.svg" alt="" />
</p>

<h1 align="center">
  🌐💻 APLICACIONES WEB ORIENTADA A SERVICIOS
</h1>

# 🎓 API Estudiantes - ITIC

API REST desarrollada en Python con Flask y PostgreSQL para el registro 
y consulta de estudiantes universitarios.

## 📋 Descripción

Este proyecto forma parte de la materia **Aplicaciones Web Orientadas 
a Servicios (ITIC 2025-2026)**. El objetivo es aprender a conectar Flask 
con una base de datos PostgreSQL y realizar operaciones básicas de 
almacenamiento y consulta a través de una API REST.

## 🎯 Propósito

Proporcionar un sistema sencillo que permita:
- Registrar estudiantes con nombre, carrera y semestre
- Consultar, buscar y filtrar estudiantes
- Actualizar y eliminar registros
- Documentar y probar la API visualmente con Swagger

## 🚀 Endpoints

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/api/estudiantes` | Obtener todos los estudiantes |
| GET | `/api/estudiantes?carrera=ITIC` | Filtrar por carrera |
| GET | `/api/estudiantes?nombre=Ana` | Buscar por nombre |
| GET | `/api/estudiantes?semestre=5` | Filtrar por semestre |
| GET | `/api/estudiantes/{id}` | Obtener un estudiante por ID |
| POST | `/api/estudiantes` | Registrar un nuevo estudiante |
| PUT | `/api/estudiantes/{id}` | Actualizar un estudiante |
| DELETE | `/api/estudiantes/{id}` | Eliminar un estudiante |

## 🛠 Tecnologías

- Python 3.14
- Flask 3.x
- PostgreSQL
- SQLAlchemy + Flask-SQLAlchemy
- Flasgger (Swagger UI)
- Flask-CORS
- python-dotenv

## ⚙️ Instalación
```bash
# Clonar el repositorio
git clone https://github.com/tu-usuario/api_estudiantes.git
cd api_estudiantes

# Crear entorno virtual
python -m venv venv
venv\Scripts\activate

# Instalar dependencias
pip install flask flask-sqlalchemy psycopg2-binary python-dotenv flasgger flask-cors
```

## 🔧 Configuración

Crea un archivo `.env` en la raíz del proyecto:
```
FLASK_ENV=development
FLASK_DEBUG=1
SECRET_KEY=clave-secreta-api-estudiantes
DATABASE_URL=postgresql://usuario:password@localhost:5432/api_estudiantes_db
```

## ▶️ Ejecutar
```bash
python run.py
```

Abre el navegador en `http://localhost:5000` para ver la documentación Swagger.

## 📁 Estructura

| Archivo | Descripción |
|---|---|
| `app/__init__.py` | Configuración principal de Flask |
| `app/models.py` | Modelo de base de datos |
| `app/routes.py` | Endpoints de la API |
| `run.py` | Punto de entrada del servidor |
| `.env` | Variables de entorno |


  ![pruebas](https://github.com/natalyvictoria-jpg/3.7.-Resolver-problema-mediante-una-API
/raw/main/db.jpeg)

    ![pruebas](https://github.com/natalyvictoria-jpg/3.7.-Resolver-problema-mediante-una-API
/raw/main/swagger.jpeg)
