class DisplayResults:

    def display_freq_text(self, freq, numResults):
        print(freq.max())
        print(freq.most_common(numResults))

    def display_freq_plot(self, freq, numResults):
        freq.plot(numResults)
