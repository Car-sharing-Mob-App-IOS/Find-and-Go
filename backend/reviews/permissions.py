from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsReviewAuthorOrReadOnly(BasePermission):
    """
    Пользователь может редактировать свой собственный отзыв,
    но только просматривать другие отзывы.
    """

    def has_object_permission(self, request, view, obj):
        # Разрешено для всех методов SAFE_METHODS (GET, HEAD, OPTIONS)
        if request.method in SAFE_METHODS:
            return True

        # Редактирование разрешено только авторам отзывов
        return obj.author == request.user
