# auth_service_app/urls.py
from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),
    path('auth/login/', views.log_in, name='login'),
    path('auth/register/', views.register, name='register'),
    path('auth/logout/', views.log_out, name='logout'),

]