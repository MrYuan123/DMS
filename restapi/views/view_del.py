from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse, HttpResponseServerError
from django.views.generic import View
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from restapi.models import *

import json

def studentDelete(request):
    query = request.POST
    studentId = query.get('id')
    try:
        Student.objects.get(id=student_id).delete()
    except Student.DoesNotExist:
        return HttpResponseBadRequest()
    except Exception:
        return HttpResponseServerError()
    return HttpResponse()

def dormitoryDelete(request):
    query = request.POST
    dormitoryId = query.get('id')
    try:
        Dormitory.objects.get(id=dormitory_id).delete()
    except Dormitory.DoesNotExist:
        return HttpResponseBadRequest()
    except Exception:
        return HttpResponseServerError()
    return HttpResponse()

def apartmentDelete(request):
    query = request.POST
    apartmentId = query.get('id')
    try:
        Apartment.objects.get(id=apartment_id).delete()
    except Apartment.DoesNotExist:
        return HttpResponseBadRequest()
    except Exception:
        return HttpResponseServerError()
    return HttpResponse()

def disciplineDelete(request):
    query = request.POST
    disciplineId = query.get('id')
    try:
        Discipline.objects.get(id=discipline_id).delete()
    except Discipline.DoesNotExist:
        return HttpResponseBadRequest()
    except Exception:
        return HttpResponseServerError()
    return HttpResponse()

def sanitationDelete(request):
    query = request.POST
    sanitationId = query.get('id')
    try:
        Sanitation.objects.get(id=sanitation_id).delete()
    except Sanitation.DoesNotExist:
        return HttpResponseBadRequest()
    except Exception:
        return HttpResponseServerError()
    return HttpResponse()

def disciplineTypeDelete(request):
    query = request.POST
    disciplineTypeId = query.get('id')
    try:
        DisciplineType.objects.get(id=discipline_type_id).delete()
    except DisciplineType.DoesNotExist:
        return HttpResponseBadRequest()
    except Exception:
        return HttpResponseServerError()
    return HttpResponse()

def adminDelete(request):
    query = request.POST
    adminId = query.get('id')
    try:
        User.objects.get(id=adminId).delete()
    except User.DoesNotExist:
        return HttpResponseBadRequest()
    except Exception:
        return HttpResponseServerError()
    return HttpResponse()


