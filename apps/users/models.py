from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        CITIZEN = 'citizen', 'Громадянин'
        OFFICER = 'officer', 'Держслужбовець'

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.CITIZEN,
    )
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.email