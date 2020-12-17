import inspect

import nltk
import re


# Class tokenizes the text given to it using regex
class TransformText:

    # Separates text by white space, and converts to lowercase
    def tokenise_text_by_space(self, text):
        words = []
        ps = "\w+"
        token_text = re.findall(ps, text)
        for word in token_text:
            words.append(word.lower())
        return words

    def remove_stopwords(self, words, lang):
        words_nostop = []
        sw = nltk.corpus.stopwords.words(lang)
        for word in words:
            if word not in sw:
                words_nostop.append(word)
        return words_nostop

# possible = os.listdir('/home/matth/corpora/stopwords')
# language in possible
