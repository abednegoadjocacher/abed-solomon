# from django import forms
# from django.contrib.auth.models import User
# from django.core.exceptions import ValidationError
# import re

# class UserRegisterForm(forms.Form):
#     fullname = forms.CharField(max_length=100)
#     username = forms.CharField(max_length=100)
#     Mobile_number = forms.CharField(max_length=15)
#     email = forms.EmailField(required=False)
#     password = forms.CharField(widget=forms.PasswordInput())
#     confirm_password = forms.CharField(widget=forms.PasswordInput())

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if email and User.objects.filter(email=email).exists():
#             raise forms.ValidationError("This email is already registered.")
#         return email

#     def clean_Mobile_number(self):
#         phone = self.cleaned_data.get('Mobile_number')
#         pattern = r'^\+?[\d]{9,15}$'
#         if not re.match(pattern, phone):
#             raise forms.ValidationError("Enter a valid mobile number.")
#         return phone

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         confirm = cleaned_data.get("confirm_password")
#         if password != confirm:
#             raise ValidationError("Passwords do not match")
#         return cleaned_data
