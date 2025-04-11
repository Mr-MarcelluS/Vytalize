from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from .forms import LoginForm, RegisterForm
from .models import UserProfile, PatientDetails, Patient, HealthRecord


def home(request):
    return render(request, 'accounts/home.html')


# ---------- LOGIN VIEWS ----------

def login_doctor(request):
    form = LoginForm(request.POST or None)
    error = ""
    if request.method == "POST" and form.is_valid():
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        if user:
            profile = UserProfile.objects.get(user=user)
            if profile.role == 'doctor':
                login(request, user)
                return redirect('dashboard_doctor')
            else:
                error = "Not a doctor account."
        else:
            error = "Invalid credentials."
    return render(request, 'accounts/login_doctor.html', {'form': form, 'error': error})


def login_patient(request):
    form = LoginForm(request.POST or None)
    error = ""
    if request.method == "POST" and form.is_valid():
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password']
        )
        if user:
            profile = UserProfile.objects.get(user=user)
            if profile.role == 'patient':
                login(request, user)
                return redirect('dashboard_patient')
            else:
                error = "Not a patient account."
        else:
            error = "Invalid credentials."
    return render(request, 'accounts/login_patient.html', {'form': form, 'error': error})


def logout_view(request):
    logout(request)
    return redirect('login_patient')


# ---------- REGISTRATION ----------

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            role = form.cleaned_data['role']
            UserProfile.objects.create(user=user, role=role)
            return redirect('login_' + role)
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


# ---------- DASHBOARDS ----------

@login_required
def dashboard_doctor(request):
    doctor = request.user
    patients = Patient.objects.filter(doctor=doctor)
    selected_patient = None
    message = None

    patient_id = request.GET.get("patient_id") or request.POST.get("patient_id")
    if patient_id:
        selected_patient = patients.filter(id=patient_id).first()

        if selected_patient:
            # Attach record if it exists
            record, created = PatientDetails.objects.get_or_create(patient=selected_patient)
            selected_patient.record = record

            if request.method == "POST":
                record.health_history = request.POST.get('health_history', '')
                record.bp = request.POST.get('bp', '')
                record.sugar = request.POST.get('sugar', '')
                record.weight = request.POST.get('weight', '')
                record.medications = request.POST.get('medications', '')
                record.save()
                message = f"✅ Health details saved for {selected_patient.name}!"

    return render(request, 'accounts/dashboard_doctor.html', {
        'doctor': doctor,
        'patients': patients,
        'selected_patient': selected_patient,
        'message': message,
    })


@login_required
def dashboard_patient(request):
    patient = request.user
    try:
        record = PatientDetails.objects.get(patient=patient)
    except PatientDetails.DoesNotExist:
        record = None

    return render(request, 'accounts/dashboard_patient.html', {
        'patient': patient,
        'record': record,
    })


# ---------- PATIENT HISTORY VIEW ----------

@login_required
def patient_history(request):
    patient_id = request.GET.get('patient_id')
    patient = Patient.objects.filter(id=patient_id).first()

    if not patient:
        return redirect('dashboard_doctor')

    if patient.doctor != request.user:
        return HttpResponseForbidden("You're not authorized to view this patient's history.")

    records = HealthRecord.objects.filter(patient=patient)
    return render(request, 'accounts/patient_history.html', {
        'patient': patient,
        'records': records
    })

from django.http import HttpResponse

@login_required
def add_patient(request):
    return HttpResponse("<h3>🛠️ Add Patient Page - Coming Soon</h3>")

from django.db import models
from django.contrib.auth.models import User

from .models import Patient, PatientDetails, HealthRecord, UserProfile


