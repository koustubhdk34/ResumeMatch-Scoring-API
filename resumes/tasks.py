from celery import shared_task
import fitz  # PyMuPDF

from .models import Resume


@shared_task
def parse_resume(resume_id):
    try:
        resume = Resume.objects.get(id=resume_id)
        doc = fitz.open(resume.file.path)
        text = ""
        for page in doc:
            text += page.get_text()
        resume.text = text
        resume.save()
        return f"Parsed resume {resume.id}"
    except Exception as e:
        return str(e)


