from rest_framework import serializers

from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Review."""

    class Meta:
        model = Review
        fields = [
            "id",
            "score",
            "user",
            "car",
            "comment"
            ]

    def validate_score(self, value):
        """
        Проверка, что значение оценки находится
        в допустимом диапазоне [0, 5]
        и что оценка является числом.
        """
        if not isinstance(value, (int, float)):
            raise serializers.ValidationError(
                "Значение оценки должно быть числом."
            )
        if not (0 <= value <= 5):
            raise serializers.ValidationError(
                "Значение оценки должно быть в диапазоне от 0 до 5."
            )
        return value
