from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse, HttpResponseServerError
from django.views.generic import View
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from restapi.models import *

import json
import datetime
from django.db import transaction

def studentAdd(request):
    try:
        query = request.POST
        dormitory_id = query.get('dormitory_id')

        with transaction.atomic():
            dorm = Dormitory.objects.get(pk=dormitory_id)

            if dorm.gender != query.get('gender'):
                return HttpResponseBadRequest()

            if not(request.user.is_superuser or Manage.objects.get(admin_id=request.user.id).dormitory_id == dormitory_id):
                return HttpResponseBadRequest()

            if dorm.capacity == len(dorm.student_set.all()):
                return HttpResponseBadRequest()

            newStudent = Student(
                id=query.get('id'),
                name=query.get('name'),
                paid=int(query.get('paid')),
                dormitory_id=query.get('dormitory_id'),
                gender=query.get('gender'),
                reside_date=query.get('reside_date')
            )
            record = MoveDormitory(
                student_id=query.get('id'), des_dorm_id=query.get('dormitory_id'),
                admin_id=request.user.id, date=query.get('reside_date')
            )
            newStudent.save()
            record.save()
    except Exception as e:
        print(e)
        return HttpResponseBadRequest()
    return HttpResponse()

def dormitoryAdd(request):
    query = request.POST
    try:
        newDormitory = Dormitory(
            id=query.get('id'),
            apartment_id=query.get('apartment_id'),
            capacity=query.get('capacity'),
            balance=query.get('balance'),
            gender=query.get('gender'),
        )
        newDormitory.save()
    except Exception:
        return HttpResponseBadRequest()
    return HttpResponse()

def apartmentAdd(request):
    query = request.POST
    try:
        newApartment = Apartment(
            id=int(query.get('id')),
            name=query.get('name')
        )
        newApartment.save()
    except Exception:
        return HttpResponseBadRequest()
    return HttpResponse()


def disciplineAdd(request):
    query = request.POST
    try:
        newDiscripline = Discipline(
            id=None,
            description=query.get('description'),
            date=query.get('date'),
            student_id=query.get('student_id'),
            admin_id=int(query.get('admin_id')),
            dis_type_id=int(query.get('type_id'))
        )
        newDiscripline.save()
    except Exception as e:
        return HttpResponseBadRequest()
    return HttpResponse()

def sanitationAdd(request):
    query = request.POST
    try:
        newSanitation = Sanitation(
            id=None,
            dormitory_id=query.get('dormitory_id'),
            admin_id=query.get('admin_id'),
            date=query.get('date'),
            score=query.get('score'),
            comment=query.get('comment')
        )
        newSanitation.save()
    except Exception as e:
        return HttpResponseBadRequest()
    return HttpResponse()

def disciplineTypeAdd(request):
    query = request.POST
    try:
        newDisciplineType = DisciplineType(
            id=None,
            name=query.get('name')
        )
        newDisciplineType.save()
    except Exception as e:
        return HttpResponseBadRequest()
    return HttpResponse()


def adminAdd(request):
    query = request.POST
    try:
        newAdmin = User.objects.create_user(
            username=query.get('username'),
            password=query.get('password'),
            is_superuser=int(query.get('is_superuser')),
            is_staff=True,
            is_active=True
        )
        newAdmin.save()
    except Exception as e:
        return HttpResponseBadRequest()
    return HttpResponse()


