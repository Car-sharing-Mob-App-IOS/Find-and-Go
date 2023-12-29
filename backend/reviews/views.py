from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Review
from .serializers import ReviewSerializer


@extend_schema(tags=["Отзывы"])
@extend_schema_view(
    list=extend_schema(summary="Список отзывов"),
    create=extend_schema(summary="Создание отзыва"),
)
class ReviewListCreateView(ModelViewSet):
    """Представление для работы с отзывами пользователей."""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination
    permission_classes = [AllowAny]
    filter_backends = [
        DjangoFilterBackend,
    ]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )


@extend_schema(tags=["Отзывы"])
@extend_schema_view(
    retrieve=extend_schema(summary="Получение одного отзыва"),
)
class ReviewDetailView(ModelViewSet):
    """Представление для получения конкретного отзыва пользователя."""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]
    filter_backends = [
        DjangoFilterBackend,
    ]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
