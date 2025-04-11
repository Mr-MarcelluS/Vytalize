from django.contrib import admin
from .models import DoctorProfile, Patient, MedicalHistory, Prescription, MedicalReport

@admin.register(DoctorProfile)
class DoctorProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialization', 'contact_number')
    search_fields = ('user__username', 'specialization')

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'doctor', 'age', 'gender')
    search_fields = ('first_name', 'last_name', 'doctor__user__username')
    list_filter = ('gender', 'doctor')

@admin.register(MedicalHistory)
class MedicalHistoryAdmin(admin.ModelAdmin):
    list_display = ('patient', 'diagnosis', 'date')
    search_fields = ('patient__first_name', 'patient__last_name', 'diagnosis')
    list_filter = ('date',)

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'date')
    search_fields = ('patient__first_name', 'doctor__user__username')
    list_filter = ('date',)

@admin.register(MedicalReport)
class MedicalReportAdmin(admin.ModelAdmin):
    list_display = ('patient', 'uploaded_at', 'description')
    search_fields = ('patient__first_name', 'description')
    list_filter = ('uploaded_at',)
