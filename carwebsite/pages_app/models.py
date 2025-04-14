from django.db import models #type: ignore
from django.contrib.auth.models import User #type: ignore
from django.core.validators import RegexValidator #type: ignore

class user_Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Only 10-digit numbers allowed
    mobile = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message="Enter a valid 10-digit mobile number",
                code='invalid_mobile'
            )
        ]
    )

    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"

    def __str__(self):
        return self.user.username
