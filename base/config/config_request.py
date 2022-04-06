import datetime
from enum import Enum


class RequestConfig(Enum):
    REQUEST_URL = "https://www.carqueryapi.com/api/0.3/?callback=?&cmd=getTrims&year={}".format(datetime.datetime.now().year)
    HEADERS = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
