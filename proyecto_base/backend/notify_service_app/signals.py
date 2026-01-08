from django.db.models.signals import post_save
from django.dispatch import receiver
from stress.models import Notification  # Importamos el modelo existente
from .tasks import send_notification_email # Importamos nuestra tarea de Celery

@receiver(post_save, sender=Notification)
def trigger_email_on_notification_save(sender, instance, created, **kwargs):
    """
    Escucha la señal 'post_save' para el modelo Notification.
    """
    # Nos aseguramos de que solo se ejecute cuando se crea una notificación nueva
    if created:
        user = instance.user
        subject = 'Nueva notificación de StressTrack'
        message = instance.message # Usamos el mensaje del objeto Notificación

        # Llamamos a nuestra tarea de Celery de forma asíncrona
        # Usamos .delay() para que se ejecute en segundo plano
        send_notification_email.delay(user.id, subject, message)