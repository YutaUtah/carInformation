from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from .config.config_request import RequestConfig
from .fetch import FetchAPI

# Create your views here.


def index(request):
    responded_API_object = FetchAPI(RequestConfig.REQUEST_URL.value, RequestConfig.HEADERS.value)
    context = {
        'cars': responded_API_object.get_carlist(),
    }
    import os
    from pathlib import Path
    BASE_DIR = Path(__file__).resolve().parent.parent
    print(os.path.join(BASE_DIR, 'templates'))
    return render(request, "pages/index.html", context)