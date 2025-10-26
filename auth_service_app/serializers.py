# auth_service_app/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.hashers import make_password

CustomUser = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'first_name', 'last_name', 'dni', 'role')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate_password(self, value: str) -> str:
        """
        Hashea la contraseña.
        """
        return make_password(value)

    def create(self, validated_data):
        # Aseguramos que los usuarios creados por esta vía no sean superusuarios
        validated_data['is_superuser'] = False
        validated_data['is_staff'] = False
        return super().create(validated_data)

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Personaliza el token para incluir roles (exp y iat ya están incluidos).
    """
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Añadir claims personalizados (payload)
        token['email'] = user.email
        token['role'] = user.role # ¡Requisito de roles cumplido!
        # 'exp' y 'iat' son añadidos automáticamente por SimpleJWT

        return token