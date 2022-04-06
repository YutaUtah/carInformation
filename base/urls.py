from django.urls import path

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.get_car_image, name='carImage'),
    path('modelList/<str:car_model>', views.get_model_list, name='carModel'),
]