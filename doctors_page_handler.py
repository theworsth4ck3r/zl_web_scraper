import uuid
from urllib.parse import urlparse
from http_client import HttpClient
from html_parser import HTMLDocumentParser
from csv_writer import CsvWriter


class DoctorsPageHandler:
    def __init__(self, specialization_name: str, page: int):
        self.page = page
        self.specialization_name = specialization_name
        self.http_client = HttpClient()
        self.csv_writer = CsvWriter(f"{specialization_name}.csv")

    def get_doctors_data(self) -> None:
        _DOCTORS_LIST = []

        _response = self.http_client.send_request(
            self.http_client.get_doctor_list_url(self.specialization_name, self.page)
        )

        _HTML_PARSER = HTMLDocumentParser(_response)

        doctor_items = _HTML_PARSER.select(
            "[data-id='result-item'][data-test-entity-type='doctor']"
        )

        for _item in doctor_items:
            _specialization, _city_name = (
                self.get_city_name_and_specialization_from_path(
                    _item.get("data-doctor-url")
                )
            )

            phone_number = self.get_phone_number_from_doctor_page(
                _item.get("data-doctor-url")
            )

            if phone_number:
                _DOCTORS_LIST.append({
                    "uuid": uuid.uuid4(),
                    "name": _item.get("data-doctor-name"),
                    "specialization": _specialization,
                    "city": _city_name,
                    "phone": phone_number
                })

        self.csv_writer.write_rows(_DOCTORS_LIST)

    def get_phone_number_from_doctor_page(self, doctor_page_url: str):
        _parser = HTMLDocumentParser(self.http_client.send_request(doctor_page_url))

        _elements = _parser.select("[data-patient-app-event-name='dp-call-phone']")

        if len(_elements):
            return _elements[0].get("href").lstrip("tel:")

    def get_city_name_and_specialization_from_path(self, path: str):
        path = urlparse(path).path
        parts = [p for p in path.split("/") if p]

        last_two = parts[-2:]

        return last_two[0], last_two[1]
