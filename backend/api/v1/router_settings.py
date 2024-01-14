from rest_framework import routers


# Здесь хранятся исключенные действия для CustomDjoserUserRouter
EXCLUDED_ACTIONS = {
    # "users-list",
    "users-activation",
    "users-me",
    # "users-detail",
    "users-resend-activation",
    "users-set-password",
    "users-reset-password",
    "users-reset-password-confirm",
    "users-set-username",
    "users-reset-username",
    "users-reset-username-confirm",
    # "api-root",
}


class CustomDjoserUserRouter(routers.DefaultRouter):
    """
    Кастомный роутер для пользовательских эндпоинтов Djoser.
    Исключает определенные действия из стандартного набора URL.
    """

    def get_urls(self):
        urls = super().get_urls()
        urls = [url for url in urls if url.name not in EXCLUDED_ACTIONS]

        return urls
