# Para iniciar el proyecto movil
## Iniciar Proyecto
### 1. Se nesesita instalar Android Studio
Android Studio [https://developer.android.com/studio?authuser=2&hl=es-419]
### 2. Crear entorno virtual
```python
python -m venv venv
```
### 3. Entrar entorno virtual

```python
venv\Scripts\activate
```
### 4. Instalar requirements
```python
pip install - r requirements
```
### 5. Iniciar proyecto

```python
python manage.py runserver 0.0.0.0:8000
```

## Crear carpeta para Android Studio
### 1. Crear la estructura del proyecto móvil
```python
mkdir stresstrack_mv
cd stresstrack_mv

npm init -y
```

### 2. Instalar Capacitor
```python
npm install @capacitor/core @capacitor/cli @capacitor/android
```

### 3. Inicializar Capacitor
```python
npx cap init
```
#### - Te preguntará Name: stresstrack_mv
#### - Te preguntará Package ID: com.stresstrack.app
#### - Te preguntará Web asset directory: www

### 4. Configurar capacitor.config.json
```json
{
  "appId": "com.stresstrack.app",
  "appName": "stresstrack_mv",
  "webDir": "www",
  "server": {
    "url": "http://10.0.2.2:8000",
    "cleartext": true
  }
}

```
### 5. Guardar los datos
```python
npx cap sync
```

### 6. Correr el servidor
```python
python manage.py runserver 0.0.0.0:8000
```

### 7. Generar la app movil
```python
npx cap add android

npx cap open android
```