from rest_framework import serializers

from .validators import state_number_validate
from .models import Car, CoordinatesCar, CarVarious


class CoordinatesCarSerializer(serializers.ModelSerializer):
    """Сериализатор для модели CoordinatesCar."""

    class Meta:
        model = CoordinatesCar
        fields = ("latitude", "longitude")


class CarVariousSerializer(serializers.ModelSerializer):
    """Сериализатор для модели CarVarious."""

    class Meta:
        model = CarVarious
        fields = ("id", "name", "slug")


class CarSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Car."""

    coordinates = CoordinatesCarSerializer()
    various = serializers.SlugRelatedField(
        many=True,
        slug_field="slug",
        queryset=CarVarious.objects.all(),
    )
    # various = CarVariousSerializer(many=True)

    class Meta:
        model = Car
        fields = [
            "id",
            "image",
            "coordinates",
            "is_available",
            "model",
            "company",
            "brand",
            "type_car",
            "state_number",
            "type_engine",
            "various",
            "power_reserve",
            "rating",
            "kind_car",
        ]

    def create_or_update_coordinates(self, instance, coordinates_data):
        """
        Создает или обновляет координаты автомобиля.
        """
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
        """
        Создает новый объект Car с указанными данными.
        """
        various_values = validated_data.pop("various", [])
        coordinates_data = validated_data.pop("coordinates", {})

        coordinates_instance = self.create_or_update_coordinates(
            None,
            coordinates_data,
        )

        validated_data["coordinates"] = coordinates_instance
        state_number_validate(validated_data["state_number"])

        car = Car.objects.create(**validated_data)
        car.various.set(various_values)

        return car

    def update(self, instance, validated_data):
        """
        Обновляет существующий объект Car с указанными данными.
        """
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
        """
        Преобразует объект Car в представление для API.
        """
        data = super().to_representation(instance)
        data["rating"] = float(data["rating"])

        return data
