from django.shortcuts import render #type: ignore
from .models import Car

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'shop_app/index.html', {'cars': cars})

def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    return render(request, 'shop_app/car_detail.html', {'car': car})

# def shop(request):
    # return render(request, 'shop_app/index.html')