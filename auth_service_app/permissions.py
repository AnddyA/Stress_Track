# auth_service_app/permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsTeacher(BasePermission):
    """
    Permiso personalizado para verificar si el usuario tiene el rol 'teacher'.
    """
    message = "Acceso denegado. Se requiere rol de 'teacher'."

    def has_permission(self, request, view):
        # request.user es el usuario decodificado del token JWT
        return request.user and request.user.role == 'teacher'

class IsStudent(BasePermission):
    """
    Permiso personalizado para verificar si el usuario tiene el rol 'student'.
    """
    message = "Acceso denegado. Se requiere rol de 'student'."

    def has_permission(self, request, view):
        return request.user and request.user.role == 'student'
    
class IsAdminUser(BasePermission):
    """
    Permiso personalizado para verificar si el usuario tiene el rol 'superuser'.
    """
    message = "Acceso denegado. Se requieren permisos de administrador."

    def has_permission(self, request, view):
        return request.user and request.user.role == 'superuser'