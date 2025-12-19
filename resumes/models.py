from django.db import models
from accounts.models import User
import uuid


def resume_upload_path(instance, filename):
    return f"resumes/{instance.user.id}/{filename}"




class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="resumes")
    file = models.FileField(upload_to=resume_upload_path)
    text = models.TextField(blank=True)  # will store parsed text
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.file.name}"
 
