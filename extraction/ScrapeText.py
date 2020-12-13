from bs4 import BeautifulSoup

# Class extracts main body of text from the supplied url
# TODO extend functionality to extract certain features of the page to be used with GetPages


class ScrapeText:
    scraped_text = []

    # Extracts the text from the supplied list of pages
    def extract_text(self, page_text_list):
        for html in page_text_list:
            scraper = BeautifulSoup(html, "html5lib")
            self.scraped_text.append(scraper.title)
            print(scraper.title)
