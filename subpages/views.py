from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect

def index(request):
    return render(request, 'subpages/index.html', { 'user': request.user })

def studentAdd(request):
    return render(request, 'subpages/student_add.html', { 'user': request.user })

def dormitoryAdd(request):
    return render(request, 'subpages/dormitory_add.html', { 'user': request.user })

def apartmentAdd(request):
    return render(request, 'subpages/apartment_add.html', { 'user': request.user })

def disciplineAdd(request):
    return render(request, 'subpages/discipline_add.html', { 'user': request.user })

def sanitationAdd(request):
    return render(request, 'subpages/sanitation_add.html', { 'user': request.user })

def disciplineTypeAdd(request):
    return render(request, 'subpages/discipline_type_add.html', { 'user': request.user })

def adminAdd(request):
    return render(request, 'subpages/administrator_add.html', { 'user': request.user })




def studentManage(request):
    return render(request, 'subpages/student.html')

def dormitoryManage(request):
    return render(request, 'subpages/dormitory.html')

def disciplineManage(request):
    return render(request, 'subpages/discipline.html')

def sanitationManage(request):
    return render(request, 'subpages/sanitation.html')

def disciplineTypeManage(request):
    return render(request, 'subpages/discipline_type.html')

def apartmentManage(request):
    return render(request, 'subpages/apartment.html')

def adminManage(request):
    return render(request, 'subpages/administrator.html')