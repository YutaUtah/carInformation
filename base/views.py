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
        'cars_list': responded_API_object.get_carlist(),
        # cars_set to remove the duplicated car maker
        'cars_set': set(car.maker for car in responded_API_object.get_carlist()),
    }
    # print(set(car.maker for car in responded_API_object.get_carlist()))
    return render(request, "pages/index.html", context)


def get_car_image(request):
    name_to_img_dict = {}
    file_list = [filename for filename in os.listdir(CarMap.CAR_IMG_DIR) if not filename.startswith('.')]
    for file in file_list:
        # getting rid of ".jpg"
        name_to_img_dict[file[:-4]] = file
    context = {
        'files': name_to_img_dict,
    }
    return render(request, "pages/carList.html", context)


def get_model_list(request, car_model):
    responded_API_object = FetchAPI(RequestConfig.REQUEST_URL.value, RequestConfig.HEADERS.value)
    car_model_list = responded_API_object.get_carlist(car_model)

    context = {
        'cars': car_model_list,
        # one car maker/car image to many car model
        'car_maker': car_model_list[0].maker,
        'car_img_jpg': CarMap.CAR_TO_IMG[car_model_list[0].maker]
    }
    return render(request, "pages/modelList.html", context)
