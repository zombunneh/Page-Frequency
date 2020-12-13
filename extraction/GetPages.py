import requests


class GetPages:
    page_text_list = []

    # fetches a specified webpage or webpages
    def fetch_pages(self, pages):
        for page in pages:
            response = requests.get(page)
            self.page_text_list.append(response.text)
