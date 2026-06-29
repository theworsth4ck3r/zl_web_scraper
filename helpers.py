from html_parser import HTMLDocumentParser
from http_client import HttpClient


class Helpers:
    def __init__(self):
        self.http_client = HttpClient()

    def get_doctors_list_max_pages(self, doctor_page_url: str):
        _parser = HTMLDocumentParser(self.http_client.send_request(doctor_page_url))

        _link_elements = _parser.select("[data-test-id='listing-pagination'] ul li a")

        _last_element = _link_elements[len(_link_elements) - 1].getText(strip=True)

        if _last_element is int:
            return int(_last_element)
        else:
            return _link_elements[len(_link_elements) - 2].getText(strip=True)
