
from django.apps import AppConfig

class NotifyServiceAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notify_service_app'

    def ready(self):
        # Importa las señales cuando la app esté lista
        import notify_service_app.signals