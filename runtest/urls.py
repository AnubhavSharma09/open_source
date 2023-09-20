from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("apppage/home", views.apppage, name="apppage"),
    path("apppage/home/onewayanova", views.onewayanova, name="onewayanova"),
    path("apppage/home/OneWayAnova", views.onewayanova, name="onewayanova"),
    path("apppage/home/upload_file", views.upload_file, name="upload_file"),
    path("apppage/home/Regression", views.regressions, name="Regressions"),
    path("retests/", views.retests, name="retests"),
    path("test_data", views.test_data, name="test_data"),
]