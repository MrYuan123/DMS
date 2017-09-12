from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout

@login_required(login_url='login/')
def mainPage(request):
    return redirect('/subpage/index')

class UserLogin(View):
    def get(self, request):
        return render(request, 'login/login.html')
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        return redirect('/')


def userLogout(request):
    logout(request)
    return redirect('/login')