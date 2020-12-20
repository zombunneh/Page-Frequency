class ExportResults:

    def save_as_txt(self, word_list):
        f = open("word_list.txt", "w+")
        for word, freq in word_list:
            temp_word = word + ' ' + (str(freq))
            f.write(temp_word + '\n')
        f.close()


    def save_as_csv(self, word_list):
        word_list
