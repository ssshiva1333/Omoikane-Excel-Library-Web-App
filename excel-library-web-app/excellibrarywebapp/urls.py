from django.urls import path
from . import views

urlpatterns = [
    path("", views.mainPageView, name="main"),
    path("api/excel/add/", views.excelAPIAdd, name="excelAPIAdd"),
    path("api/excel/change/", views.excelAPIChange, name="excelAPIChange"),
    path("api/excel/remove/", views.excelAPIRemove, name="excelAPIRemove"),
    path("api/excel/get/", views.excelAPIGet, name="excelAPIGet"),
    path("api/excel/backup/", views.excelAPIBackup, name="excelAPIBackup")
]