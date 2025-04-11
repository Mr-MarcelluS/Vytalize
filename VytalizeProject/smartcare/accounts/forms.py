from django import forms
from .models import DoctorProfile, Patient, MedicalHistory, Prescription, MedicalReport

# Doctor Profile Form
class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = ['specialization', 'contact_number', 'profile_picture']


# Patient Profile Form
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = [
            'first_name', 'last_name', 'phone_number', 'address',
            'blood_group', 'allergies', 'medical_conditions'
        ]


# Medical History Form
class MedicalHistoryForm(forms.ModelForm):
    class Meta:
        model = MedicalHistory
        fields = ['diagnosis', 'treatment']


# Prescription Form
class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['medication', 'dosage', 'instructions']


# Medical Report Form
class MedicalReportForm(forms.ModelForm):
    class Meta:
        model = MedicalReport
        fields = ['report_name', 'report_file']
