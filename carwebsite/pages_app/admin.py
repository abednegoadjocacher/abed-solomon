from django.contrib import admin #type: ignore
from .models import user_Profile
# Register your models here.
admin.site.register(user_Profile)