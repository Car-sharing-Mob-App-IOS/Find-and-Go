from django.db.transaction import atomic
from drf_spectacular.utils import extend_schema, extend_schema_view

from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Car
from .serializers import CarSerializer
from .filters import CarFilter
from django_filters.rest_framework import DjangoFilterBackend


@extend_schema(tags=["Машины"])
@extend_schema_view(
    list=extend_schema(summary="Список машин"),
    retrieve=extend_schema(summary="Получение одной машины"),
    create=extend_schema(summary="Создание машины"),
    update=extend_schema(summary="Полное обновление машины"),
    partial_update=extend_schema(summary="Частичное обновление машины"),
    destroy=extend_schema(summary="Удаление машины"),
)
class CarViewSet(ModelViewSet):
    """Представление для работы с публичными данными автомобилей."""

    queryset = Car.objects.all()
    serializer_class = CarSerializer
    pagination_class = PageNumberPagination
    permission_classes = [AllowAny]
    filter_backends = [
        DjangoFilterBackend,
    ]
    filterset_class = CarFilter

    @atomic
    def create(self, request, *args, **kwargs):
        """Создать новый автомобиль."""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers,
        )

    @atomic
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance=instance,
            data=request.data,
            partial=partial,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)
