import qrcode
import os
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.mail import send_mail
from django.conf import settings
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.core.files.storage import default_storage


def generate_qr_code(data, filename="qr_code.png"):
    """
    Generate a QR code image from data and return the file path.
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    file_path = os.path.join("qr_codes", filename)
    default_storage.save(file_path, ContentFile(buffer.getvalue()))
    return file_path


def generate_pdf(content_dict, filename="document.pdf"):
    """
    Generate a PDF file from a dictionary of content and return the file path.
    """
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=A4)
    text = p.beginText(40, 800)
    text.setFont("Helvetica", 12)

    for key, value in content_dict.items():
        line = f"{key}: {value}"
        text.textLine(line)

    p.drawText(text)
    p.showPage()
    p.save()

    file_path = os.path.join("pdfs", filename)
    default_storage.save(file_path, ContentFile(buffer.getvalue()))
    return file_path


def send_notification_email(subject, message, recipient_email):
    """
    Send an email notification to a specific email address.
    """
    from_email = settings.DEFAULT_FROM_EMAIL
    send_mail(
        subject,
        message,
        from_email,
        [recipient_email],
        fail_silently=False,
    )
