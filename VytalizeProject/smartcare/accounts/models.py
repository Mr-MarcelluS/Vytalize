from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('doctor', 'Doctor'),
        ('patient', 'Patient'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_patients')

    def __str__(self):
        return self.name


class HealthRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    condition = models.TextField()
    date = models.DateField(auto_now_add=True)

class PatientDetails(models.Model):
    patient = models.OneToOneField(User, on_delete=models.CASCADE)
    health_history = models.TextField()
    bp = models.CharField(max_length=20)
    sugar = models.CharField(max_length=20)
    weight = models.CharField(max_length=20)
    medications = models.TextField()

    def __str__(self):
        return f"{self.name} ({self.patient_id})"  # ❌ Not indented


