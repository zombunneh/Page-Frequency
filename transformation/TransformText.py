import nltk
import re


# Class tokenizes the text given to it using regex
class TransformText:
    words = []

    # Separates text by white space, and converts to lowercase
    def tokenise_text_by_space(self, text):
        ps = '\w+'
        token_text = re.findall(ps, text)
        for word in token_text:
            self.words.append(word.lower())
