from rest_framework import serializers

from .models import Car, CoordinatesCar
from .validators import state_number_validate


class CoordinatesCarSerializer(serializers.ModelSerializer):
    """Сериализатор для модели CoordinatesCar."""

    class Meta:
        model = CoordinatesCar
        fields = ("latitude", "longitude")


class CarSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Car."""

    coordinates = CoordinatesCarSerializer()

    class Meta:
        model = Car
        fields = "__all__"

    def create_or_update_coordinates(self, instance, coordinates_data):
        """Создает или обновляет координаты автомобиля."""
        if instance:
            coordinates_serializer = CoordinatesCarSerializer(
                instance.coordinates,
                data=coordinates_data,
                partial=True,
            )
        else:
            coordinates_serializer = CoordinatesCarSerializer(
                data=coordinates_data,
                partial=True,
            )
        coordinates_serializer.is_valid(raise_exception=True)
        return coordinates_serializer.save()

    def create(self, validated_data):
        """Создает новый объект Car с указанными данными."""
        coordinates_data = validated_data.pop("coordinates", {})
        coordinates_instance = self.create_or_update_coordinates(
            None, coordinates_data
        )
        validated_data["coordinates"] = coordinates_instance

        state_number_validate(validated_data["state_number"])

        car = Car.objects.create(**validated_data)
        return car

    def update(self, instance, validated_data):
        """Обновляет существующий объект Car с указанными данными."""
        coordinates_data = validated_data.pop("coordinates", {})
        coordinates_instance = self.create_or_update_coordinates(
            instance, coordinates_data
        )
        validated_data["coordinates"] = coordinates_instance

        state_number = validated_data.get("state_number")

        if state_number:
            state_number_validate(state_number, instance)

        return super().update(instance, validated_data)

    def to_representation(self, instance):
        """Преобразует объект Car в представление для API."""
        data = super().to_representation(instance)
        data["rating"] = str(data["rating"])
        return data
