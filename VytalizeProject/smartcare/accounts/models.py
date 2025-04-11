from django.db import models
from django.contrib.auth.models import User

# Doctor Profile
class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='doctor_profiles/', blank=True, null=True)

    def __str__(self):
        return self.user.get_full_name()


# Patient Profile
class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    blood_group = models.CharField(max_length=5)
    allergies = models.TextField(blank=True, null=True)
    medical_conditions = models.TextField(blank=True, null=True)
    # other fields...


    # New fields for QR code & PDF download
    qr_code_image = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    pdf_report = models.FileField(upload_to='pdf_reports/', blank=True, null=True)

    def __str__(self):
        return self.name

# Medical History
class MedicalHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    diagnosis = models.TextField()
    treatment = models.TextField()

    def __str__(self):
        return f"{self.patient.name} - {self.date}"

# Prescription
class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    medication = models.CharField(max_length=255)
    dosage = models.CharField(max_length=100)
    instructions = models.TextField()
    prescribed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription for {self.patient.name}"


# Medical Report
class MedicalReport(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    report_name = models.CharField(max_length=100)
    file = models.FileField(upload_to='medical_reports/')

    def __str__(self):
        return f"{self.patient.name} - {self.report_name}"
