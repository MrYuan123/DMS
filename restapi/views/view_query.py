from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse, HttpResponseServerError
from django.views.generic import View
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from restapi.models import *

import json

def studentQuery(request):
    query = request.POST
    studentId = query.get('id', None)
    name = query.get('name', None)
    paid = query.get('paid', None)
    dormitory_id = query.get('dormitory_id', None)
    gender = query.get('gender', None)
    reside_date = query.get('reside_date', None)

    students = Student.objects.all()
    try:
        if studentId:
            student = Student.objects.get(pk=studentId)
            students = [student]
        else:
            if name:
                students = students.filter(name=name)
            if paid:
                students = students.filter(paid=paid)
            if dormitory_id:
                students = students.filter(dormitory_id=dormitory_id)
            if gender:
                students = students.filter(gender=gender)
            if reside_date:
                students = students.filter(reside_date=reside_date)

        ret_data = list()
        for student in students:
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
        
    except Exception as e:
        return HttpResponseBadRequest()


def dormitoryQuery(request):
    query = request.POST

    dormitoryId = query.get('id', None)
    apartment_id = query.get('apartment_id', None)
    capacity = query.get('capacity', None)
    balance = query.get('balance', None)
    gender = query.get('gender', None)

    dormitories = Dormitory.objects.all()
    try:
        if dormitoryId:
            dormitory = Dormitory.objects.get(pk=dormitoryId)
            dormitories = [dormitory]
        else:
            if apartment_id:
                dormitories = dormitories.filter(apartment_id=apartment_id)
            if capacity:
                dormitories = dormitories.filter(capacity=capacity)
            if balance:
                dormitories = dormitories.filter(balance=balance)
            if gender:
                dormitories = dormitories.filter(gender=gender)

        ret_data = list()
        for dormitory in dormitories:
            dormitory_dict = {
                'id': dormitory.id,
                'apartment_id': dormitory.apartment.id,
                'capacity': dormitory.capacity,
                'balance': dormitory.balance,
                'gender': dormitory.gender
            }   
            ret_data.append(dormitory_dict)
        return JsonResponse({'dormitory': ret_data})
        
    except Exception:
        return HttpResponseBadRequest()


def disciplineQuery(request):
    query = request.POST

    disciplineId = query.get('id', None)
    date = query.get('date', None)
    student_id = query.get('student_id', None)
    admin_id = query.get('admin_id', None)
    dis_type_id=query.get('type_id', None)
    disciplines = Discipline.objects.all()
    try:
        if disciplineId:
            discipline = Discipline.objects.get(pk=disciplineId)
            disciplines = [discipline]
        else:
            if date:
                disciplines = disciplines.filter(date=date)
            if student_id:
                disciplines = disciplines.filter(student_id=student_id)
            if admin_id:
                disciplines = disciplines.filter(admin_id=admin_id)
            if dis_type_id:
                disciplines = disciplines.filter(dis_type_id=dis_type_id)

        ret_data = list()
        for discipline in disciplines:
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
        
    except Exception:
        return HttpResponseBadRequest()

def sanitationQuery(request):
    query = request.POST
    
    sanitationId = query.get('id', None)
    dormitory_id = query.get('dormitory_id', None)
    admin_id = query.get('admin_id', None)
    date = query.get('date', None)
    score = query.get('score', None)

    sanitations = Sanitation.objects.all()
    try:
        if sanitationId:
            sanitation = Sanitation.objects.get(pk=sanitationId)
            sanitations = [sanitation]
        else:
            if dormitory_id:
                sanitations = sanitations.filter(dormitory_id=dormitory_id)
            if admin_id:
                sanitations = sanitations.filter(admin_id=admin_id)
            if date:
                sanitations = sanitations.filter(date=date)
            if score:
                sanitations = sanitations.filter(score=score)
        ret_data = list()
        for sanitation in sanitations:
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
    except Exception:
        return HttpResponseBadRequest()

