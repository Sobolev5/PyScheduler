from django.urls import re_path
from snippet import views

app_name = "snippet"

urlpatterns = [
    re_path(r"^list/$", views.snippet_list, name="snippet_list"),
    re_path(r"^add/$", views.snippet_edit, name="snippet_add"),
    re_path(r"^edit/(?P<snippet_id>\w+)/$", views.snippet_edit, name="snippet_edit"),
]
