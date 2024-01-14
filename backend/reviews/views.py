from django_filters.rest_framework import DjangoFilterBackend

from drf_spectacular.utils import extend_schema, extend_schema_view

from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from .models import Review
from .permissions import IsReviewAuthorOrReadOnly
from .serializers import ReviewSerializer


@extend_schema(tags=["Отзывы"])
@extend_schema_view(
    list=extend_schema(
        summary="Получить список отзывов",
        description="Возвращает список отзывов пользователей.",
    ),
    retrieve=extend_schema(
        summary="Получить отзыв по ID",
        description="Позволяет получить отдельный отзыв "
        "по его уникальному идентификатору.",
    ),
)
class ReviewViewSet(ModelViewSet):
    """Представление для работы с отзывами пользователей."""

    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination
    permission_classes = [IsReviewAuthorOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["user", "rating"]
    http_method_names = ["get"]
