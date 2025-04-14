import re
from django.contrib.auth import authenticate, login #type: ignore
from .models import user_Profile 
from django.contrib.auth.models import User, auth #type: ignore
from django.contrib import messages #type: ignore
from django.shortcuts import render, redirect #type: ignore


# this is to validate if the password meet requirement
def validate_password(password):
    errors = []
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")
    if not re.search(r'[A-Z]', password):
        errors.append("Password must contain at least one uppercase letter.")
    if not re.search(r'[a-z]', password):
        errors.append("Password must contain at least one lowercase letter.")
    if not re.search(r'[0-9]', password):
        errors.append("Password must contain at least one digit.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        errors.append("Password must contain at least one special character.")
    
    return errors



def create_account(request):
    if request.method == 'POST':
        # fullname =request.POST.get('full_name').strip()
        username =request.POST.get('username')
        phone_number =request.POST.get('Mobile_number')
        email =request.POST.get('email')
        password =request.POST.get('password')
        password = request.POST.get('password')
        confirm_password =request.POST.get('confirm_password')


        if password != confirm_password:
            messages.info(request, "Password did not match")
            return redirect('create_account')
        
        error_list = validate_password(password)
        if error_list:
            for error in error_list:
                messages.error(request, error)
            return redirect('create_account')
        
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already exist")
            return redirect('create_account')
        
        if user_Profile.objects.filter(mobile=phone_number):
            messages.info(request, "Number already exist")
            return redirect('create_account')
        
        # if User.objects.filter(full_name=full_name).exists():
            # messages.info(request, "Name already in used")
            # return redirect('create_account')
        
        if User.objects.filter(email=email).exists():
            messages.info(request, "Email already Used")
            return redirect('create_account')

        

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            # full_name=full_name
        )
        user.save()
        return redirect('login')
    else:
        return render(request, 'pages_app/create_account.html')
        


def home(request):
    return render(request, 'pages_app/index.html')

def contact(request):
    return render(request, 'pages_app/contact.html')

def login(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        username = request.POST.get('username')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')  # redirect to homepage or dashboard
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('login')  # back to login page
    return render(request, 'pages_app/login.html')



def logout(request):
    auth.logout(request)
    return redirect('home')
