# proyecto/celery.py
import os
from celery import Celery

# Establece el módulo de settings de Django para el 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proyecto.settings')

app = Celery('proyecto')

# Usa un string aquí para que el worker no tenga que serializar
# el objeto de configuración.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Carga automáticamente módulos de tareas de todas las apps registradas.
app.autodiscover_tasks()