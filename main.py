# In here we call our methods to create the following workflow:
# Query user to search through 1 page or multiple pages
# Access the page(s)
# Scrape the text from it (relevant text only?)
# Compile a frequency list of words from the page
# Translate text from specified language to english
# Display the results to the user
# Export the results for use elsewhere e.g. anki deck (formatted in csv/txt etc)

# Future improvements
# TODO: add functionality to read a collection of webpages from a master page rather than having to add specific pages

import validators
from extraction.GetPages import GetPages


def main():
    url_list = []

    print('Enter a URL or multiple URL\'s, separated by a new line and press enter when done:')

    sentinel = ''
    for url_input in iter(input, sentinel):
        if not validators.url(url_input):
            print('This is not a valid url, please input a valid url or end input')
            pass
        url_list.append(url_input)
        print(url_list)

    page_fetcher = GetPages()
    page_fetcher.fetch_pages(url_list)


if __name__ == '__main__':
    main()

