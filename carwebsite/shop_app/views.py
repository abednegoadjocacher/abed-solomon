from django.shortcuts import render

# Create your views here.
def shop(request):
    return render(request, 'shop_app/index.html')