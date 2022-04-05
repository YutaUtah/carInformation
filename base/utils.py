import os

from .config.config_car import CarMap

def is_different_car_object(dict_car_info, car_list):
    if 1 <= len(car_list):
        if dict_car_info['model_make_id'] == car_list[-1].maker and dict_car_info['model_name'] == car_list[-1].model:
            return False
    return True


def generate_car_image_dir(each_car_info):
    return CarMap.CAR_TO_IMG[each_car_info['model_make_id']]