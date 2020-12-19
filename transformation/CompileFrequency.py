import nltk
import seaborn as sb


class CompileFrequency:

    # Returns a frequency distribution of the words in the supplied list
    def calculate_word_freq(self, words):
        sb.set()
        freqdist = nltk.FreqDist(words)
        return freqdist
