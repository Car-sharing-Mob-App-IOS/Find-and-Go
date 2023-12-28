from cars.views import CarViewSet
from django.urls import include, path
from drf_spectacular.views import SpectacularSwaggerView
from rest_framework import routers
from social_django import urls as social_django_urls
from users.views import PublicUserViewSet

from .router_settings import CustomDjoserUserRouter

app_name = "api"

# Routers v1
router_v1 = routers.DefaultRouter()
user_router_v1 = CustomDjoserUserRouter()

# Register
user_router_v1.register("users", PublicUserViewSet, "users")
router_v1.register("cars", CarViewSet, "cars")


# URL
urlpatterns = [
    path("", include(router_v1.urls)),
    path("", include(user_router_v1.urls)),
    path("auth/", include("djoser.urls.authtoken")),
    path("swagger/", SpectacularSwaggerView.as_view(), name="swagger"),
    path('auth/', include(social_django_urls), name='social'),
]
