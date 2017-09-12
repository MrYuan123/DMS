from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/', views.UserLogin.as_view()),
    url(r'^logout/', views.userLogout),
    url(r'^$', views.mainPage),
]
