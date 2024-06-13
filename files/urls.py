from django.urls import path

from . import views

app_name = "files"
urlpatterns = [
    path("", views.index, name="index"),
    path("detail/<int:file_id>", views.detail, name="detail"),
    path("upload", views.upload, name="upload"),
]
