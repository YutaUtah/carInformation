from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.get_car_image, name='carimage'),
]