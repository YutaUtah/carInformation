import os

from django.shortcuts import render
from django.views.decorators.http import require_GET

from .config.config_car import CarMap
from .config.config_request import RequestConfig
from .fetch import FetchAPI


# Create your views here.
@require_GET
def index(request):
    request_url = RequestConfig.REQUEST_URL.value
    header_value = RequestConfig.HEADERS.value
    responded_api_object = FetchAPI(request_url, header_value)

    context = {
        'cars_list': responded_api_object.get_carlist(),
        # cars_set to remove the duplicated car maker
        'cars_set': set(car.maker for car in responded_api_object.get_carlist()),
    }
    # print(set(car.maker for car in responded_api_object.get_carlist()))
    return render(request, "pages/index.html", context)


@require_GET
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


@require_GET
def get_model_list(request, car_model):
    request_url = RequestConfig.REQUEST_URL.value
    header_value = RequestConfig.HEADERS.value
    responded_api_object = FetchAPI(request_url, header_value)
    car_model_list = responded_api_object.get_carlist(car_model)

    context = {
        'cars': car_model_list,
        # one car maker/car image to many car model
        'car_maker': car_model_list[0].maker,
        'car_img_jpg': CarMap.CAR_TO_IMG[car_model_list[0].maker]
    }
    return render(request, "pages/modelList.html", context)
