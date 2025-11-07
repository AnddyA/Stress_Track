from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings
from stress.models import CustomUser # Importas el modelo de usuario

@shared_task
def send_notification_email(user_id, subject, message):
    """
    Tarea de Celery para enviar un correo de notificación.
    """
    try:
        user = CustomUser.objects.get(id=user_id)
        if user.email:
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER, # El remitente (stresstrackservice@gmail.com)
                [user.email],             # El destinatario
                fail_silently=False,
            )
        return f"Correo enviado a {user.email}"
    except CustomUser.DoesNotExist:
        return f"Usuario con id {user_id} no encontrado."
    except Exception as e:
        # Manejar errores de envío (opcional, pero recomendado)
        return f"Error al enviar correo: {str(e)}"