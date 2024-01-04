from rest_framework import serializers

from .utils import validate_score
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Review."""

    score = serializers.FloatField(validators=[validate_score])

    class Meta:
        model = Review
        fields = [
            "id",
            "score",
            "user",
            "car",
            "comment",
        ]


class AddReviewSerializer(serializers.ModelSerializer):
    score = serializers.FloatField(validators=[validate_score])

    class Meta:
        model = Review
        fields = [
            "score",
            "comment",
        ]
