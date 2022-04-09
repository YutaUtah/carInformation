import json
import requests

from .utils import is_different_car_object, generate_car_image_dir


class Car:
    def __init__(self, maker, model, image_jpg):
        self.maker = maker
        self.model = model
        self.image_jpg = image_jpg

    def __eq__(self, other):
        if not isinstance(other, Car):
            return False
        return self.maker == other.maker and self.model == other.model


class FetchAPI:
    def __init__(self, requested_url, headers):
        self.requested_url = requested_url
        self.headers = headers


    @property
    def _fetched_API(self):
        # request API and convert it to json schema
        response = requests.get(self.requested_url, headers=self.headers)
        return json.loads(response.text[11:-3])


    def get_carlist(self, car_model=None):
        car_list = []
        for each_car_info in self._fetched_API:
            # remove duplicated car object using is_different_car_object
            # create Car class with appropriate variables
            if is_different_car_object(each_car_info, car_list):
                obtained_car_object = Car(
                                        each_car_info['model_make_id'],
                                        each_car_info['model_name'],
                                        generate_car_image_dir(each_car_info)
                                      )
                # store car object to car_list
                if car_model is None or obtained_car_object.maker.lower() == car_model.lower():
                    car_list.append(obtained_car_object)

        return car_list
