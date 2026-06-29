from bs4 import BeautifulSoup


class HTMLDocumentParser:
    def __init__(self, _html_response: str):

        # Use lxml parser if available (faster), fallback to html.parser
        try:
            self.soup = BeautifulSoup(_html_response, "lxml")
        except Exception:
            self.soup = BeautifulSoup(_html_response, "html.parser")

    def select(self, selector: str):
        return self.soup.select(selector)
