from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Home page (Landing page for logged-in users)
    path('', views.home, name='home'),

    # Registration view (for doctors)
    path('register/', views.register, name='register'),

    # Login views for both doctor and patient
    path('login_doctor/', views.login_doctor, name='login_doctor'),
    path('login_patient/', views.login_patient, name='login_patient'),

    # Dashboard for doctors (after login)
    path('dashboard_doctor/', views.dashboard_doctor, name='dashboard_doctor'),
    
    # Dashboard for patients (after login)
    path('dashboard_patient/', views.dashboard_patient, name='dashboard_patient'),

    # Add patient (Only doctors can access)
    path('add_patient/', views.add_patient, name='add_patient'),

    # Patient history view
    path('patient_history/', views.patient_history, name='patient_history'),

    # Password reset views
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),

    # User logout
    path('logout/', views.logout_user, name='logout'),

    path('patient/<int:patient_id>/history/', views.patient_history, name='patient_history'),

    # New Features
    path('patient/<int:patient_id>/generate_pdf/', views.generate_pdf_view, name='generate_pdf'),
    path('patient/<int:patient_id>/generate_qr/', views.generate_qr_code_view, name='generate_qr'),
    path('patient/<int:patient_id>/send_email/', views.send_email_alert, name='send_email'),
]
