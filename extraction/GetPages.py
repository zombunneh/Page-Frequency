import requests


class GetPages:
    page_text_list = []

    # fetches a specified webpage or webpages
    def fetch_pages(self, pages):
        for page in pages:
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
            response = requests.get(page, headers=headers)
            self.page_text_list.append(response.text)
