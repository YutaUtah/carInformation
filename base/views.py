import os

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .config.config_request import RequestConfig
from .config.config_car import CarMap
from .fetch import FetchAPI


# Create your views here.
def index(request):
    responded_API_object = FetchAPI(RequestConfig.REQUEST_URL.value, RequestConfig.HEADERS.value)
    context = {
        'cars': responded_API_object.get_carlist(),
    }
    return render(request, "pages/index.html", context)


def get_car_image(request):
    files = os.listdir('base/static/img')
    context = {
        'files': files,
    }
    return render(request, "pages/carList.html", context)


def get_model_list(request, car_model):
    responded_API_object = FetchAPI(RequestConfig.REQUEST_URL.value, RequestConfig.HEADERS.value)
    car_model_list = responded_API_object.get_carlist(car_model)

    context = {
        'cars': car_model_list,
        'car_img_jpg': CarMap.CAR_TO_IMG[car_model_list[0].maker]
    }
    return render(request, "pages/modelList.html", context)