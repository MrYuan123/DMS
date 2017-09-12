from django.conf.urls import url
from django.contrib import admin
from .views import view_del, view_add, view_query, view_queryall, view_change

urlpatterns = [
    url(r'^student/change_dormitory/', view_change.changeDormitory),

    url(r'^student/delete/', view_del.studentDelete),
    url(r'^dormitory/delete/', view_del.dormitoryDelete),
    url(r'^apartment/delete/', view_del.apartmentDelete),
    url(r'^discipline/delete/', view_del.disciplineDelete),
    url(r'^sanitation/delete/', view_del.sanitationDelete),
    url(r'^discipline_type/delete/', view_del.disciplineTypeDelete),
    url(r'^administrator/delete/', view_del.adminDelete),
    # ...


    url(r'^student/add/', view_add.studentAdd),
    url(r'^dormitory/add/', view_add.dormitoryAdd),
    url(r'^apartment/add/', view_add.apartmentAdd),
    url(r'^discipline/add/', view_add.disciplineAdd),
    url(r'^sanitation/add/', view_add.sanitationAdd),
    url(r'^discipline_type/add/', view_add.disciplineTypeAdd),
    url(r'^administrator/add/', view_add.adminAdd),


    url(r'^student_table/', view_queryall.studentQueryAll),
    url(r'^dormitory_table/', view_queryall.dormitoryQueryAll),
    url(r'^apartment_table/', view_queryall.apartmentQueryAll),
    url(r'^discipline_table/', view_queryall.disciplineQueryAll),
    url(r'^sanitation_table/', view_queryall.sanitationQueryAll),
    url(r'^discipline_type_table/', view_queryall.disciplineTypeQueryAll),
    url(r'^administrator_table/', view_queryall.adminQueryAll),



    url(r'^student/inquire/', view_query.studentQuery),
    url(r'^dormitory/inquire/', view_query.dormitoryQuery),
    url(r'^discipline/inquire/', view_query.disciplineQuery),
    url(r'^sanitation/inquire/', view_query.sanitationQuery),
]
