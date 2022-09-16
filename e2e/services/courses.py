from urllib.parse import urljoin
import requests
from requests import Response


API_URL = "http://localhost:9303"


class Courses:

    def __init__(self):
        pass

    def get_courses(self, params=None) -> Response:
        """
        request to check a GCP reverse image search result
        :return:
        """
        response = requests.get(
            urljoin(API_URL, f'/courses?{params}')
        )

        return response
