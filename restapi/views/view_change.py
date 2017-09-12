from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse, HttpResponseServerError
from django.views.generic import View
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from restapi.models import *

import datetime
import json
from django.db import transaction

@transaction.atomic
def changeDormitory(request):
    student_id = request.POST.get('id', None)
    des_dormitory_id = request.POST.get('des_dormitory_id', None)
    student = Student.objects.get(id=student_id)
    
    if student.dormitory_id == des_dormitory_id:
        return HttpResponseBadRequest()

    des_dormitory = Dormitory.objects.get(pk=des_dormitory_id)
    if len(des_dormitory.student_set.all()) == des_dormitory.capacity:
        return HttpResponseBadRequest()

    if des_dormitory.gender != student.gender:
        return HttpResponseBadRequest()

    if des_dormitory.apartment_id != student.dormitory.id and not request.user.is_superuser:
        return HttpResponseBadRequest()

    # safe to change
    src_dorm_id = student.dormitory_id
    student.dormitory_id = des_dormitory_id
    student.save()
    now = datetime.datetime.now()

    record = MoveDormitory(student_id=student_id, src_dorm_id=src_dorm_id, des_dorm_id=des_dormitory_id,
        admin_id=request.user.id, date=datetime.date(now.year, now.month, now.day))
    record.save()
    return HttpResponse()