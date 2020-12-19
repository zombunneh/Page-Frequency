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

from display.DisplayResults import DisplayResults
from display.ExportResults import ExportResults
from extraction.GetPages import GetPages
from extraction.ScrapeText import ScrapeText
from transformation.CompileFrequency import CompileFrequency
from transformation.TransformText import TransformText


def main():
    url_list = []

    print('Enter a URL or multiple URL\'s, separated by a new line and press enter when done:')

    # Accepts user input until enter is pressed on a blank line
    sentinel = ''
    for url_input in iter(input, sentinel):
        if not validators.url(url_input):
            print('This is not a valid url, please input a valid url or end input')
            continue
        url_list.append(url_input)

    page_fetcher = GetPages()
    page_fetcher.fetch_pages(url_list)  # Fetch html representation of the url list supplied

    text_scraper = ScrapeText()
    text_scraper.extract_text(page_fetcher.page_text_list)  # Create a more readable text from the html supplied
    text = text_scraper.scraped_text

    text_transformer = TransformText()
    word_list = text_transformer.tokenise_text_by_space(text)  # Returns a list of words separated by whitespace
    word_list_ns = text_transformer.remove_stopwords(word_list, 'english')  # Remove stopwords from the list in given language

    freq_compiler = CompileFrequency()
    freq_list = freq_compiler.calculate_word_freq(word_list_ns)  # Returns a frequency distribution of all the words in the list supplied

    results_display = DisplayResults()
    # Get user input to determine the number of results to display, repeat input if an int is not the input
    while True:
        try:
            numResults = int(input('Input the number of results to display\n'))
        except ValueError:
            print('That\'s not an int!')
            continue
        else:
            if validators.between(numResults, 0):
                break
            continue
    results_display.display_freq_plot(freq_list, numResults)  # Plots the frequency distribution
    results_display.display_freq_text(freq_list, numResults)  # Prints the most common word, and a list of the most common words

    results_exporter = ExportResults()
    print('Would you like to save these results?')


if __name__ == '__main__':
    main()

