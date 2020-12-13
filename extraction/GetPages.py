import requests


class GetPages:

    # fetches a specified webpage or webpages
    def fetch_pages(self, pages):
        print("fetch_page called")
        for page in pages:
            response = requests.get(page)
            type(response)
