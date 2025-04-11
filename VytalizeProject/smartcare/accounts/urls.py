from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('login/doctor/', views.login_doctor, name='login_doctor'),
    path('login/patient/', views.login_patient, name='login_patient'),
    path('dashboard/doctor/', views.dashboard_doctor, name='dashboard_doctor'),
    path('dashboard/patient/', views.dashboard_patient, name='dashboard_patient'),
    path('doctor/patient-history/', views.patient_history, name='patient_history'),
    path('doctor/add-patient/', views.add_patient, name='add_patient'),

]