import requests


class HttpClient:
    def send_request(self, url: str):
        _response = requests.get(url, timeout=10)
        _response.raise_for_status()

        return _response.text

    def get_doctor_list_url(self, specialization_name: str, page: int = 1):
        return f"https://www.znanylekarz.pl/szukaj?q={specialization_name}&page={page}"
