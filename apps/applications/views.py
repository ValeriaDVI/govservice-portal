from rest_framework import viewsets, permissions
from .models import Application
from .serializers import ApplicationSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Це виправляє попередження Swagger
        if getattr(self, 'swagger_fake_view', False):
            return Application.objects.none()
        
        user = self.request.user
        if user.role == 'officer':
            return Application.objects.all()
        return Application.objects.filter(applicant=user)

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)