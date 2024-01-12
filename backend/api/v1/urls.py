from cars.views import CarViewSet
from django.urls import include, path
from drf_spectacular.views import SpectacularSwaggerView
from rest_framework import routers
from reviews.views import ReviewViewSet
from users.views import (CustomTokenCreateView, CustomTokenDestroyView,
                         PublicUserViewSet)

from .router_settings import CustomDjoserUserRouter

app_name = "api"

# Routers v1
router_v1 = routers.DefaultRouter()
user_router_v1 = CustomDjoserUserRouter()

# Register
user_router_v1.register("users", PublicUserViewSet, "users")
router_v1.register("cars", CarViewSet, "cars")
router_v1.register("reviews", ReviewViewSet, "reviews")


# URL
urlpatterns = [
    path("", include(router_v1.urls)),
    path("", include(user_router_v1.urls)),
    path("auth/", include("djoser.social.urls")),
    path("swagger/", SpectacularSwaggerView.as_view(), name="swagger"),
    path('auth/token/login/',
         CustomTokenCreateView.as_view(),
         name='login'),
    path('auth/token/logout/',
         CustomTokenDestroyView.as_view(),
         name='logout'),
]
