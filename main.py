from doctors_page_handler import DoctorsPageHandler
from http_client import HttpClient
from helpers import Helpers


def run():
    _http_client = HttpClient()
    _helpers = Helpers()

    _SPECIALIZATION_NAME = "psycholog"
    _FIRST_PAGE = 1
    _LAST_PAGE = _helpers.get_doctors_list_max_pages(
        _http_client.get_doctor_list_url(_SPECIALIZATION_NAME, 1)
    )

    # Example - downloads given page
    # TODO: add queue of pages range, add threading
    doctors_page_handler = DoctorsPageHandler("psycholog", 70)
    doctors_page_handler.get_doctors_data()


if __name__ == "__main__":
    run()
