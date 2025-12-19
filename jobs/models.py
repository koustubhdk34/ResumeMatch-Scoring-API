from django.db import models
from accounts.models import User


class JobDescription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="job_descriptions")
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.user.email}"
