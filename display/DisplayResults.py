class DisplayResults:

    def display_freq_text(self, freq):
        print(freq.max())
        print(freq.most_common(5))

    def display_freq_plot(self, freq):
        freq.plot(25)
