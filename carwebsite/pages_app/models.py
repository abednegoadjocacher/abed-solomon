from django.db import models #type:ignore

# Create your models here.
from django.contrib.auth.models import AbstractUser #type:ignore
from django.db import models #type:ignore
from django.core.exceptions import ValidationError #type:ignore

class CustomUser(AbstractUser):
    email = models.EmailField(blank=True, null=True, unique=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True, unique=True)

    def clean(self):
        if not self.email and not self.phone_number:
            raise ValidationError("Provide either email or phone number.")
        if self.email and self.phone_number:
            raise ValidationError("Provide only one: email or phone number.")

        def __str__(self):
            return self.username
