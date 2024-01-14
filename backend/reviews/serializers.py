from rest_framework import serializers

from .utils import validate_raiting
from .models import Review


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
    rating = serializers.FloatField(validators=[validate_raiting])

    class Meta:
        model = Review
        fields = [
            "rating",
            "comment",
        ]
