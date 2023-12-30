from django.db.transaction import atomic
from django.db import IntegrityError

from django_filters.rest_framework import DjangoFilterBackend

from drf_spectacular.utils import extend_schema, extend_schema_view

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.texts import ADD_REVIEW_SUCCESS, REVIEW_ALREADY_EXISTS
from reviews.serializers import AddReviewSerializer

from .filters import CarFilter
from .models import Car
from .serializers import CarSerializer


@extend_schema(tags=["Машины"])
@extend_schema_view(
    list=extend_schema(summary="Список машин"),
    retrieve=extend_schema(summary="Получение одной машины"),
    create=extend_schema(summary="Создание машины"),
    update=extend_schema(summary="Полное обновление машины"),
    partial_update=extend_schema(summary="Частичное обновление машины"),
    destroy=extend_schema(summary="Удаление машины"),
    add_review=extend_schema(summary="Добавление отзыва к автомобилю."),
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

    def perform_create(self, serializer, car):
        serializer.save(car=car, user=self.request.user)

    def get_serializer_class(self):
        if self.action == "add_review":
            return AddReviewSerializer
        else:
            return CarSerializer

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
        """Обновить данные об автомобиле."""
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

    @action(
        detail=True,
        methods=["POST"],
        permission_classes=[IsAuthenticated],
    )
    def add_review(self, request, pk=None):
        """Добавление отзыва к автомобилю."""
        car = self.get_object()
        serializer = self.get_serializer(data=request.data)

        try:
            if serializer.is_valid():
                serializer.save(car=car, user=request.user)
                response_data = {
                    "message": ADD_REVIEW_SUCCESS,
                    "review": serializer.data,
                }
                return Response(response_data, status=status.HTTP_201_CREATED)

        except IntegrityError:
            return Response(
                {"message": REVIEW_ALREADY_EXISTS},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
