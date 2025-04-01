from django.shortcuts import render #type: ignore

# Create your views here.
def home(request):
    return render(request, 'pages_app/index.html')

def contact(request):
    return render(request, 'pages_app/contact.html')