from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    applicant = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Application
        fields = ['id', 'title', 'description', 'status', 'applicant', 'created_at']
        read_only_fields = ['status', 'applicant', 'created_at']