from django.urls import path

from . import views

app_name = 'base'


urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.get_car_image, name='car_image'),
    path('modelList/<str:car_model>/', views.get_model_list, name='modelList'),
]