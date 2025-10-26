# auth_service_app/urls.py
from django.urls import path
from . import views


urlpatterns = [

    path('', views.home, name='home'),
    path('auth/login/', views.log_in, name='login'),
    path('auth/register/', views.register, name='register'),
    path('auth/profile/', views.profile, name='profile'),
    path('auth/logout/', views.log_out, name='logout'),

    path('panel/', views.panel, name='panel'),
    path('tasks/', views.list_tasks, name='list-tasks'),
    path('tests/', views.list_tests, name='list-test'),
    path('course/', views.course, name='course'),
    path('users/', views.user_admin, name='users'),


    path('user/state/udate/<int:user_id>/', views.change_state_user, name='change-user-state'),
    path('user/desactivate/', views.desactivate_account_notification, name='desactivate-account'),

]