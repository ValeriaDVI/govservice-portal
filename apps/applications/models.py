from django.db import models
from apps.users.models import User

class Application(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'draft', 'Чернетка'
        SUBMITTED = 'submitted', 'Подана'
        IN_REVIEW = 'in_review', 'На розгляді'
        APPROVED = 'approved', 'Схвалена'
        REJECTED = 'rejected', 'Відхилена'

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.DRAFT,
    )
    applicant = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='applications',
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} — {self.status}"