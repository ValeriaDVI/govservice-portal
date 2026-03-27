from django.contrib import admin
from .models import Application

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'applicant', 'created_at']
    list_filter = ['status']
    search_fields = ['title', 'applicant__username']
