from rest_framework import serializers

from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id', 'resume', 'job', 'status', 'similarity_score', 'applied_at']
        read_only_fields = ['similarity_score', 'applied_at']

    def create(self, validated_data):
        app = super().create(validated_data)
        from applications.utils import calculate_similarity
        from .tasks import send_application_reminder
        app.similarity_score = calculate_similarity(app.resume.text, app.job.description)
        app.save()
        send_application_reminder.delay(app.id)
        return app

