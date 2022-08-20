import debug_toolbar
from django.conf.urls import handler404
from django.conf.urls import handler500
from django.contrib import admin
from django.urls import include
from django.urls import path
from django.urls import re_path

from settings import DEBUG


urlpatterns = [path("admin/", admin.site.urls), path("i18n/", include("django.conf.urls.i18n"))]


urlpatterns += [
    re_path(r"", include("main.urls", namespace="main")),
    re_path(r"^snippet/", include("snippet.urls", namespace="snippet")),
    re_path(r"^profile/", include("user_profile.urls", namespace="user_profile")),
]


handler404 = "main.views.handler404"
handler500 = "main.views.handler500"


if DEBUG:
    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
    ]
