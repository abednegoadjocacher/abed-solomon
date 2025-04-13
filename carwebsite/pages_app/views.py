import re
from django.contrib.auth import authenticate, login #type: ignore
from .forms import UserRegisterForm
#from .models import CustomUser
from django.contrib.auth.models import User, auth #type: ignore
from django.contrib import messages #type: ignore
from django.shortcuts import render, redirect #type: ignore
#from .models import UserProfile  # if I would be saving the phone number here

def create_account(request):
    if request.method == 'POST':
        # fullname =request.POST.get('full_name').strip()
        username =request.POST.get('username')
        phone_number =request.POST.get('Mobile_number')
        email =request.POST.get('email')
        password =request.POST.get('password')
        confirm_password =request.POST.get('confirm_password')


        if password != confirm_password:
            messages.info(request, "Password did not match")
            return redirect('create_account')
        
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already exist")
            return redirect('create_account')
        
        # if User.objects.filter(full_name=full_name).exists():
            # messages.info(request, "Name already in used")
            # return redirect('create_account')
        
        if len(password) <= 6:
            messages.info(request, "Password must be more than six characters")
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
        
        # form = UserRegisterForm(request.POST)
        # 
        # if form.is_valid():
            # Get cleaned data from form
            # username = form.cleaned_data['username']
            # email = form.cleaned_data['email']
            # password = form.cleaned_data['password']
            # fullname = form.cleaned_data['fullname']
            # phone = form.cleaned_data['Mobile_number']
            # 
            # Create the user
            # user = User.objects.create_user(
                # username=username,
                # email=email,
                # password=password,
                # phone=phone,
            # )
            # Split full name into first and last
            # name_parts = fullname.strip().split()

            # Always assign the first name
            # user.first_name = name_parts[0]

            # If there's more than one name part, assign the rest as last name
            # if len(name_parts) > 1:
                # user.last_name = " ".join(name_parts[1:])

            # user.save()
            # Optional: Save phone number in a UserProfile model
            # UserProfile.objects.create(user=user, phone_number=phone)

            # Show success message and redirect
            # messages.success(request, "Account created successfully! You can now log in.")
            # return redirect('login')  # URL name for your login page

        # else:
            # If form is not valid, show error messages
            # messages.error(request, "Please correct the errors below.")
    
    # else:
        # form = UserRegisterForm()

    # return render(request, 'pages_app/create_account.html', {'form': form})







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









#def create_account_a(request):
#    if request.method == 'POST':
#        name = request.POST['fullname']
#        password = request.POST['password']
#        confirm_password = request.POST['confirm_password']
#        mobile_number = request.POST['Mobile_number']
#        email = request.POST['email']
#        if password == confirm_password:
#            if not email_or_number:
#                messages.error(request, "Please provide either an email or a phone number.")
#                return redirect(request, 'create_account')
#            
#            if re.match(r"[^@]+@[^@]+\.[^@]+", email_or_number):
#                email = email_or_number
#                phone_number = None
#
#            elif re.match(r"^\+?[0-9]{10,15}$", email_or_number): 
#                email = None
#                phone_number = email_or_number
#            else:
#                messages.error(request, "Please provide a valid email or phone number.")
#                return redirect(request, 'create_account')
#            
#            if not email and not phone_number:
#                messages.error(request, "Please provide either an email or a phone number.")
#                return redirect(request, 'create_account')
#            
#            if email and phone_number:
#                messages.error(request, "You can only provide one: either email or phone number.")
#                return redirect(request, 'create_account')
#
#            if User.objects.filter(email_or_number=email_or_number).exists():
#                messages(request, " Email Already Used")
#                return redirect('create_account')
#            elif User.objects.filter(full_name=full_name).exists():
#                messages.info(request, "Named Already Exist")
#                return redirect('create_account')
#            else:
#                
#                user = CustomUser.objects.create_user(
#                full_name=full_name,
#                password=password,
#                email=email if email else None,
#                phone_number=phone_number if phone_number else None )
#                login(request, user)
#                return redirect('login')  # or any success URL
#
#
#                # user = User.objects.create_user(email=email_or_number, full_name=full_name, password=password)
#               # user.save()
#        else:
#            messages.info(request, "Password Not Same")
#            return redirect('create_account')
#    else:       
#        return render(request, 'pages_app/create_account.html')
#    
#