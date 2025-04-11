from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

from .models import Patient, MedicalHistory, MedicalReport
from .forms import MedicalReportForm

import io
from reportlab.pdfgen import canvas
import qrcode
from django.core.files.base import ContentFile
from django.utils.timezone import now


# --- Add Patient View (with Report Upload) ---
@login_required
def add_patient(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        history_text = request.POST.get('history')
        report_file = request.FILES.get('report_file')  # Optional

        patient = Patient.objects.create(
            name=name,
            age=age,
            gender=gender,
            doctor=request.user
        )

        if history_text:
            MedicalHistory.objects.create(
                patient=patient,
                doctor=request.user,
                diagnosis='N/A',
                treatment=history_text,
                date=now()
            )

        if report_file:
            MedicalReport.objects.create(
                patient=patient,
                report_file=report_file
            )

        messages.success(request, 'Patient added successfully.')
        return redirect('dashboard_doctor')

    return render(request, 'accounts/add_patient.html')


# --- View Patient History ---
@login_required
def patient_history(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    history = MedicalHistory.objects.filter(patient=patient).order_by('-date')
    reports = MedicalReport.objects.filter(patient=patient)

    return render(request, 'accounts/patient_history.html', {
        'patient': patient,
        'history': history,
        'reports': reports
    })


# --- Generate PDF View ---
@login_required
def generate_pdf_view(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    history = MedicalHistory.objects.filter(patient=patient)

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    p.setFont("Helvetica-Bold", 16)
    p.drawString(100, 800, f"Medical History for {patient.name}")

    y = 770
    for record in history:
        p.setFont("Helvetica", 12)
        p.drawString(80, y, f"Date: {record.date.strftime('%Y-%m-%d')}")
        y -= 20
        p.drawString(100, y, f"Diagnosis: {record.diagnosis}")
        y -= 20
        p.drawString(100, y, f"Treatment: {record.treatment}")
        y -= 30
        if y < 100:
            p.showPage()
            y = 800

    p.showPage()
    p.save()
    buffer.seek(0)

    return HttpResponse(buffer, content_type='application/pdf')


# --- Generate QR Code View ---
@login_required
def generate_qr_code_view(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    qr_data = f"Patient: {patient.name}, Age: {patient.age}, Gender: {patient.gender}"
    qr = qrcode.make(qr_data)
    img_io = io.BytesIO()
    qr.save(img_io, format='PNG')
    img_content = ContentFile(img_io.getvalue(), f"{patient.name}_qr.png")

    patient.qr_code.save(f"{patient.name}_qr.png", img_content)
    patient.save()

    messages.success(request, "QR Code generated and saved.")
    return redirect('patient_history', patient_id=patient.id)


# --- Send Email Alert ---
@login_required
def send_email_alert(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)

    if patient.email:
        subject = f"SmartCare - Health Update for {patient.name}"
        message = render_to_string('accounts/email_template.html', {
            'patient': patient
        })

        send_mail(
            subject,
            '',
            settings.EMAIL_HOST_USER,
            [patient.email],
            html_message=message,
            fail_silently=False
        )

        messages.success(request, 'Email sent successfully.')
    else:
        messages.warning(request, 'Patient email not found.')

    return redirect('patient_history', patient_id=patient.id)
