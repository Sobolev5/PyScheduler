from django.urls import re_path
from user_profile import views

app_name = "user_profile"

urlpatterns = [
    re_path(r"^edit/$", views.edit_profile, name="edit_profile"),
]
