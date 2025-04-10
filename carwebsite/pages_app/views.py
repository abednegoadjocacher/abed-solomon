import re
from django.contrib.auth import login#type: ignore
from .models import CustomUser
from django.contrib.auth.models import User, auth #type: ignore
from django.contrib import messages #type: ignore
from django.shortcuts import render, redirect #type: ignore

# Create your views here.

#def login(request):
    # if request.method == 'POST':
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # email_or_number = request.POST.get('email_or_number')

        # Basic validation to ensure the field is not empty
        # if not email_or_number:
            # messages.error(request, "Please provide either an email or a phone number.")
            # return render(request, 'signup.html')

        # Check if the input is an email
        # if re.match(r"[^@]+@[^@]+\.[^@]+", email_or_number):  # simple regex for email
            # email = email_or_number
            # phone_number = None
        # Check if the input is a phone number (this can be adjusted based on your format)
        # elif re.match(r"^\+?[0-9]{10,15}$", email_or_number):  # simple regex for phone number
            # email = None
            # phone_number = email_or_number
        # else:
            # messages.error(request, "Please provide a valid email or phone number.")
            # return render(request, 'signup.html')

        # Ensure only one is provided, either email or phone
        # if not email and not phone_number:
            # messages.error(request, "Please provide either an email or a phone number.")
            # return render(request, 'signup.html')

        # if email and phone_number:
            # messages.error(request, "You can only provide one: either email or phone number.")
            # return render(request, 'signup.html')

        # Create the user
        # user = CustomUser.objects.create_user(
            # username=username,
            # password=password,
            # email=email if email else None,
            # phone_number=phone_number if phone_number else None
        # )
        # login(request, user)
        # return redirect('home')  # or any success URL

    # return render(request, 'signup.html')







def home(request):
    return render(request, 'pages_app/index.html')

def contact(request):
    return render(request, 'pages_app/contact.html')

def login(request):
    if request.method == 'POST':
        password = request.POST['password']
        full_name = request.POST['full_name']
    return render(request, 'pages_app/login.html')

def create_account(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        password = request.POST['password']
        confirm_password = request.POST['confirm']
        email_or_number = request.POST['number_email']
        if password == confirm_password:
            if not email_or_number:
                messages.error(request, "Please provide either an email or a phone number.")
                return redirect(request, 'create_account')
            
            if re.match(r"[^@]+@[^@]+\.[^@]+", email_or_number):
                email = email_or_number
                phone_number = None

            elif re.match(r"^\+?[0-9]{10,15}$", email_or_number): 
                email = None
                phone_number = email_or_number
            else:
                messages.error(request, "Please provide a valid email or phone number.")
                return redirect(request, 'create_account')
            
            if not email and not phone_number:
                messages.error(request, "Please provide either an email or a phone number.")
                return redirect(request, 'create_account')
            
            if email and phone_number:
                messages.error(request, "You can only provide one: either email or phone number.")
                return redirect(request, 'create_account')

            if User.objects.filter(email_or_number=email_or_number).exists():
                messages(request, " Email Already Used")
                return redirect('create_account')
            elif User.objects.filter(full_name=full_name).exists():
                messages.info(request, "Named Already Exist")
                return redirect('create_account')
            else:
                
                user = CustomUser.objects.create_user(
                full_name=full_name,
                password=password,
                email=email if email else None,
                phone_number=phone_number if phone_number else None )
                login(request, user)
                return redirect('login')  # or any success URL


                # user = User.objects.create_user(email=email_or_number, full_name=full_name, password=password)
               # user.save()
        else:
            messages.info(request, "Password Not Same")
            return redirect('create_account')
    else:       
        return render(request, 'pages_app/create_account.html')
    
