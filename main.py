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
# TODO: Add support for multiple languages
import os

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

    word_list = get_page_words(url_list)  # Returns a list of words from the supplied urls without the stopwords

    freq_compiler = CompileFrequency()
    freq_list = freq_compiler.calculate_word_freq(word_list)  # Returns a frequency distribution of all the words in the list supplied

    results = show_results(freq_list)  # Displays the results of the supplied frequency distribution as text and a plot according to the number of results chosen

    save_files(results, url_list)  # Gives the user the option to save files


def get_page_words(urls):
    page_fetcher = GetPages()
    page_fetcher.fetch_pages(urls)  # Fetch html representation of the url list supplied

    text_scraper = ScrapeText()
    text_scraper.extract_text(page_fetcher.page_text_list)  # Create a more readable text from the html supplied

    text_transformer = TransformText()
    word_list = text_transformer.tokenise_text_by_space(text_scraper.scraped_text)  # Returns a list of words separated by whitespace

    possible = os.listdir('C:/Users/matth/AppData/Roaming/nltk_data/corpora/stopwords')  # TODO: Change to locate  user stopwords directory

    index = 0

    for word in possible:
        index += 1
        print(f'{index}. {word}')
    print('Enter the number of the language your page(s) are in')

    language = ""

    while True:  # TODO: Implement a method of recognising what language our scraped text is automatically
        try:
            indexLang = int(input())
        except ValueError:
            print('That\'s not an int!')
            continue
        else:
            if validators.between(len(possible), 0):
                language = possible[indexLang-1]  # Correct for indexing from 0
                break
            continue

    return text_transformer.remove_stopwords(word_list, language)  # Remove stopwords from the list in given language


def show_results(freq_dist):
    results_display = DisplayResults()
    # Get user input to determine the number of results to display, repeat input if an int is not the input
    numResults = 10  # default
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
    results_display.display_freq_plot(freq_dist, numResults)  # Plots the frequency distribution
    results_display.display_freq_text(freq_dist, numResults)  # Prints the most common word, and a list of the most common words
    return results_display


def save_files(results, pages):
    results_exporter = ExportResults()
    # Get user input to determine whether to save the results of analysis
    while True:
        answer = str(input('Would you like to save these results? (y/n)')).lower().strip()
        if answer == 'y':
            results_exporter.save_as_txt(
                results.most_common_words)  # Retrieves the list of most common words and saves it to a text file
            break
        elif answer == 'n':
            break
        else:
            continue


if __name__ == '__main__':
    main()

