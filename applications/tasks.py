from celery import shared_task
from django.core.mail import send_mail

from accounts.models import User
from .models import Application


@shared_task
def send_application_reminder(application_id):
    try:
        app = Application.objects.get(id=application_id)
        subject = f"Application Update: {app.job.title}"
        message = (
            f"Hi {app.user.full_name},\n\n"
            f"Your application status for '{app.job.title}' is currently: {app.status}.\n"
            f"Similarity Score: {app.similarity_score}\n\n"
            "Regards,\nJobTrack AI"
        )
        recipient = [app.user.email]
        send_mail(subject, message, None, recipient)
        return "Email sent successfully"
    except Exception as e:
        return str(e)


