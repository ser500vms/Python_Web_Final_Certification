from django.urls import path
from .views import (
    BaseView,
    RegisterView,
    RegisteredView,
    MyLoginView,
    MyLogoutView,
)


app_name = "regapp"

urlpatterns = [
    path("", BaseView.as_view(), name="base-page"),
    path("reg/", RegisterView.as_view(), name="registration"),
    path("lk/", RegisteredView.as_view(), name="registered"),
    path("login/", MyLoginView.as_view(), name="login"),
    path("logout/", MyLogoutView.as_view(), name="logout"),
]