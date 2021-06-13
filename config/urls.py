"""planningpoker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

schema_view = get_schema_view(
    openapi.Info(
        title="Planning Poker API",
        default_version="v1",
        description="API Documentation for Realtime Planning Poker Application",
        contact=openapi.Contact(email="account+planningpokerdocs@simonalmers.com"),
    ),
    public=False,
    permission_classes=(permissions.IsAdminUser,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "auth/api-token-auth/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path("auth/api-token-refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    url(r"^api/v1/", include("users.api.urls")),
    url(r"^api/v1/", include("projects.api.urls")),
    url(r"^api/v1/", include("stories.api.urls")),
    url(
        r"^docs/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]
