from django.urls import re_path

from . import views

app_name = "main"

urlpatterns = [
    re_path(r"^$", views.user_login, name="user_login"),
    re_path(r"^auth/web3/$", views.auth_web3, name="auth_web3"),
    re_path(r"^logout/$", views.user_logout, name="user_logout"),
]
