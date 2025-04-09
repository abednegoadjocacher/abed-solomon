from django.urls import path #type: ignore
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('account/', views.create_account, name='create_account')
]