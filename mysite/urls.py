from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path("home/", include("home.urls")),
    path("hello/", include("hello.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("autos/", include("autos.urls")),
]
