from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='login.html')),
    path('login/', TemplateView.as_view(template_name='login.html')),
    path('dashboard/', TemplateView.as_view(template_name='dashboard.html')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/users/', include('apps.users.urls')),
    path('api/applications/', include('apps.applications.urls')),
    path('register/', TemplateView.as_view(template_name='register.html')),
]
