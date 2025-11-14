# Stress_Track

Este es un proyecto para gestionar y realizar tests de estrés en estudiantes.

## Requisitos

- Python 3.x
- Django 5.x
- pip
- Entorno virtual (Venv)

## Arquitectura

- Framework: Django
- Arquitectura MVC (Modelo - Vista - Controlador) adaptada a MVT de Django.
- Estructura base:  
- proyecto-base/
- ├── backend/                                                  # Código fuente del backend
- │   ├── src/                                                  #(Módulos, controladores, servicios, repositorios)
- │   ├── tests/                                                # Pruebas unitarias y de integración
- │   ├── requirements.txt                                      # o package.json según el framework
- |   ├── .env.example                                          # Variables de entorno (sin claves reales)
- ├── docs/                                                     # Documentación del proyecto
- │   ├── architecture/                                         # Diagramas C4
- │   │   ├── context-diagram.png
- │   │   ├── container-diagram.png
- │   │   └── component-diagram.png
- │   └── informe-seguridad.pdf
- ├── .github/                                                  # (Opcional) Acciones de CI/CD o plantillas
- |    ├── README.md                                            # Descripción general del proyecto
- |    ├── LICENSE                                              # Licencia
- |    └── .gitignore                                           # Archivos a excluir del control de versiones

## 🌿 Flujo GitFlow
1. Se crea rama `feature/entorno-inicial`
2. Se desarrollan cambios con commits frecuentes
3. Se finaliza la feature → merge a `develop`
4. Posteriormente, develop se fusionará con `main` para releases

## Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/Xanh1/Stress_Track.git
```

### 2. Entrar al directorio y crear un entorno virtual
```bash
cd backend_entorno
```
```bash
python -m venv venv
```

### 3. Activar el entorno virtual
* Windows:
```bash
venv\Scripts\activate
```

* Mac/Linux:
```bash
source venv/bin/activate
```

### 4. Instalar dependencias
```bash
pip install -r requirements.py
```

## Interfacez

- ✅ UI Estudiante
- ✅ UI Docente
- ✅ UI Admin

## Funcionalidades Implementadas

### Funcionalidades Completadas ✅

### Funcionalidades en Desarrollo 🚀

### Funcionalidades Pendientes ⏳


- [x] **Registro de usuario** (estudiantes)
- [x] **Log in** (estudiantes, profesores y administradores)
- [x] **Log out** (estudiantes, profesores y administradores)
- [x] **Agregar tarea** (profesores)
- [x] **Modificar tarea** (profesores)
- [x] **Eliminar tarea** (profesores)
- [x] **Visualizar tarea** (profesores, estudiantes)
- [x] **Agregar test** (profesores)
- [x] **Visualizar test** (profesores, estudiantes)
- [x] **Asignar test** (profesores)
- [x] **Realizar test** (estudiantes)
- [x] **Visualizar estado test** (estudiantes, profesores)
- [x] **Agregar grupo** (estudiantes)
- [x] **Modificar grupo** (estudiantes)
- [x] **Asignar grupo** (profesores)
- [x] **Visualizar curso** (estudiantes, profesores)
- [x] **Visualizar nivel de estres** (estudiantes, profesores)
- [x] **Compartir nivel de estres** (estudiantes)
- [x] **Editar perfil de usuario** (estudiantes, profesores)
- [x] **Restableces contraseña olvidada**: (estudiante, profesores, administradores)
- [x] **Eliminar test**: (profesores)
- [x] **Modificar test**: (profesores)
- [x] **Notificaciones**: (estudiantes, profesores, administradores)
- [x] **Registro de usuario**: (profesores, administradores)
- [x] **Agregar curso**: (administradores)
- [x] **Modificar curso**: (administradores)
- [x] **Eliminar curso**: (administradores)
- [x] **Agregar recomendacion**: (profesores, administradores)
- [x] **Modificar recomendacio**: (profesores, administradores)
- [x] **Eliminar recomendacion**: (profesores, administradores)
- [x] **Estadisticas**: (profesores, estudiantes)