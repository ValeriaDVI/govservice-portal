from django.core.cache import cache
from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Application
from .serializers import ApplicationSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Application.objects.none()
        user = self.request.user
        if user.role == 'officer':
            return Application.objects.all().select_related('applicant')
        return Application.objects.filter(applicant=user)

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)
        cache.delete(f'applications_user_{self.request.user.id}')

    def list(self, request):
        cache_key = f'applications_user_{request.user.id}'
        cached = cache.get(cache_key)
        if cached:
            return Response(cached)
        queryset = self.get_queryset()
        serializer = ApplicationSerializer(queryset, many=True)
        cache.set(cache_key, serializer.data, timeout=60)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'], url_path='change-status')
    def change_status(self, request, pk=None):
        application = self.get_object()
        if request.user.role != 'officer':
            return Response({'error': 'Недостатньо прав'}, status=status.HTTP_403_FORBIDDEN)
        new_status = request.data.get('status')
        if new_status not in dict(Application.Status.choices):
            return Response({'error': 'Невірний статус'}, status=status.HTTP_400_BAD_REQUEST)
        application.status = new_status
        application.save()
        cache.delete(f'applications_user_{application.applicant.id}')
        return Response(ApplicationSerializer(application).data)