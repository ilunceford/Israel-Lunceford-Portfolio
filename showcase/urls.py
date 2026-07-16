from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("downloads/4-bit-cpu/", views.cpu_download, name="cpu_download"),
    path("downloads/4-bit-cpu/program/", views.cpu_program_download, name="cpu_program_download"),
    path("contact/", views.contact, name="contact"),
    path("report/", views.report, name="report"),
]
