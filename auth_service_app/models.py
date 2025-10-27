from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Ingrese un correo válido')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'superuser')

        return self.create_user(email, password, **extra_fields)
    '''
    def middleware(request):
        user = getattr(request, 'user', None)
        # Se verifica que el usuario esté autenticado y que tenga rol de administrador
        if user and hasattr(user, 'role') and user.role == 'administrador':
            return get_response(request)
        
        return JsonResponse(
            {'message': 'Acceso denegado. Se requieren permisos de administrador.'},
            status=403
        )
    '''
class CustomUser(AbstractBaseUser, PermissionsMixin):

    ROLE_CHOICES = [
        ('student', 'Alumno'),
        ('teacher', 'Profesor'),
        ('superuser', 'Administrador'),
    ]

    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    dni = models.CharField(max_length=10, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='student')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    stress = models.IntegerField(default=0)
    share_stress_level = models.BooleanField(default=False)
    #recommendation = models.ForeignKey(Recommendation, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')

    #course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students', null=True, blank=True)
    #group = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members', null=True, blank=True)
    #tests = models.ManyToManyField(Test, related_name='users', blank=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    