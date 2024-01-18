from rest_framework import serializers

from .models import Review
from .utils import validate_raiting


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Review."""

    rating = serializers.FloatField(validators=[validate_raiting])

    class Meta:
        model = Review
        fields = [
            "id",
            "user",
            "car",
            "rating",
            "comment",
        ]


class AddReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для создания отзыва."""

    rating = serializers.FloatField(validators=[validate_raiting])
    created_at = serializers.DateTimeField(format="%d.%m.%Y", read_only=True)

    class Meta:
        model = Review
        fields = [
            "rating",
            "comment",
            "created_at",
        ]
