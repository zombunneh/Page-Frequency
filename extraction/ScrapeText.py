from bs4 import BeautifulSoup


class ScrapeText:
    scraped_text = []

    def extract_text(self, page_text_list):
        print("extract text called")
        for html in page_text_list:
            scraper = BeautifulSoup(html, "html5lib")
            self.scraped_text.append(scraper.title)
            print(scraper.title)
