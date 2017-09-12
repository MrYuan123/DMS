from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse, HttpResponseServerError
from django.views.generic import View
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from restapi.models import *

def studentQueryAll(request):
    ret_data = list()
    for student in Student.objects.all():
        student_dict = {
            'id': student.id,
            'name': student.name,
            'paid': student.paid,
            'dormitory_id': student.dormitory.id,
            'gender': student.gender,
            'reside_date': student.reside_date
        }
        ret_data.append(student_dict)
    return JsonResponse({'student': ret_data})

def dormitoryQueryAll(request):
    ret_data = list()
    for dormitory in Dormitory.objects.all():
        dormitory_dict = {
            'id': dormitory.id,
            'apartment_id': dormitory.apartment.id,
            'capacity': dormitory.capacity,
            'balance': dormitory.balance,
            'gender': dormitory.gender
        }
        ret_data.append(dormitory_dict)
    return JsonResponse({'dormitory': ret_data})

def disciplineQueryAll(request):
    ret_data =list()
    for discipline in Discipline.objects.all():
        discipline_dict = {
            'id': discipline.id,
            'description': discipline.description,
            'date': discipline.date,
            'student_id': discipline.student.id,
            'admin_id': discipline.admin.id,
            'type_id': discipline.dis_type.id
        }
        ret_data.append(discipline_dict)
    return JsonResponse({'discipline': ret_data})

def sanitationQueryAll(request):
    ret_data = list()
    for sanitation in Sanitation.objects.all():
        sanitation_dict = {
            'id': sanitation.id,
            'dormitory_id': sanitation.dormitory.id,
            'admin_id': sanitation.admin.id,
            'date': sanitation.date,
            'score': sanitation.score,
            'comment': sanitation.comment        
        }
        ret_data.append(sanitation_dict)
    return JsonResponse({'sanitation': ret_data})

def disciplineTypeQueryAll(request):
    ret_data = list()
    for disciplineType in DisciplineType.objects.all():
        disciplineType_dict = {
            'id': disciplineType.id,
            'name': disciplineType.name
        }
        ret_data.append(disciplineType_dict)
    return JsonResponse({'discipline_type': ret_data})

def apartmentQueryAll(request):
    ret_data = list()
    for apartment in Apartment.objects.all():
        apartment_dict = {
            'id': apartment.id,
            'name': apartment.name
        }
        ret_data.append(apartment_dict)
    return JsonResponse({'apartment': ret_data})

def adminQueryAll(request):
    ret_data = list()
    for admin in User.objects.all():
        admin_dict = {
            'id': admin.id,
            'username': admin.username,
            'super_admin': admin.is_superuser,
        }
        try:
            admin_dict['manage_apart_id'] = Manage.objects.get(admin=admin).dormitory_id
        except:
            pass
        ret_data.append(admin_dict)
    return JsonResponse({'administrator': ret_data})