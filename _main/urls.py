from argparse import Namespace
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(("api.urls", "api"), namespace="api")),
    path("user/", include(("users.urls", "users"), namespace="users")),
]
