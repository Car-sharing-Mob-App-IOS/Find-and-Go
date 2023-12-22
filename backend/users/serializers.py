from django.contrib.auth.password_validation import validate_password

from djoser.serializers import UserCreateSerializer

from rest_framework import serializers

from .models import User


class UserSerializer(UserCreateSerializer):
    """
    Сериализатор для модели пользователя .
    """

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "password",
        ]

        extra_kwargs = {
            "password": {"write_only": True},
        }

    def to_representation(self, instance):
        """
        Преобразует объект пользователя в представление JSON.
        """
        data = super().to_representation(instance)
        request = self.context.get("request")

        if request.method == "GET":
            data.pop("password", None)

        return data


class ResetCodeSerializer(serializers.Serializer):
    """
    Сериализатор для отправки кода сброса пароля по электронной почте.
    """

    email = serializers.EmailField()


class SetUserPasswordSerializer(serializers.Serializer):
    """
    Сериализатор для установки нового пароля после сброса.
    """

    email = serializers.EmailField()
    code = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate_password(self, value):
        """
        Валидация нового пароля.
        """
        validate_password(value)
        return value
