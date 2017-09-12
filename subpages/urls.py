from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^index/', index),
    url(r'^student/add/', studentAdd),
    url(r'^dormitory/add/', dormitoryAdd),
    url(r'^apartment/add/', apartmentAdd),
    url(r'^discipline/add/', disciplineAdd),
    url(r'^sanitation/add/', sanitationAdd),
    url(r'^discipline_type/add/', disciplineTypeAdd),
    url(r'^administrator/add/', adminAdd),

    url(r'^student/', studentManage),
    url(r'^dormitory/', dormitoryManage),
    url(r'^apartment/', apartmentManage),
    url(r'^discipline/', disciplineManage),
    url(r'^sanitation/', sanitationManage),
    url(r'^discipline_type/', disciplineTypeManage),
    url(r'^administrator/', adminManage),
]