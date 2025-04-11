from django.urls import path #type: ignore
from . import views
urlpatterns = [
    path('', views.car_list, name='car_list'),
    path('shop/', views.car_list, name='car_list'),
    path('shop/<int:car_id>/', views.car_detail, name='car_detail'),
]