from django.shortcuts import render #type: ignore

# Create your views here.
def home(request):
    return render(request, 'pages_app/index.html')

def contact(request):
    return render(request, 'pages_app/contact.html')

def create_account(request):
    return render(request, 'pages_app/create_account.html')

def login(request):
    full_name = request.POST['full_name']
    password = request.POST['password']
    email = request.POST['email']
    
