from django.urls import path
from . import views

urlpatterns = [
    path("register", views.CreateNewUserView.as_view(), name="register"),
]
