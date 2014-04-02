all_symbols = {}
all_words = {}


# Stores file information
class FileStats(object):

    def __init__(self, file_path):
        self.symbols = {}
        self.words = {}
        self.file_path = file_path
        self.analyze_content()

    def analyze_content(self):

        # count symbols in file content
        for char in open(self.file_path).read():

            if not ord(char) in [9, 10, 32]:
                # for a file
                try:
                    self.symbols[ord(char)] += 1
                except KeyError:
                    self.symbols[ord(char)] = 1

                # for all files together
                try:
                    all_symbols[ord(char)] += 1
                except KeyError:
                    all_symbols[ord(char)] = 1

        # count words in file content
        for word in open(self.file_path).read().split():
            if word:
               # for a file
                try:
                    self.words[word.lower()] += 1
                except KeyError:
                    self.words[word.lower()] = 1

                # for all files together
                try:
                    all_words[word.lower()] += 1
                except KeyError:
                    all_words[word.lower()] = 1

    def get_counted_content(self):
        result = self.file_path

        result += '\n\t' + 'Symbols in file'

        for symbol, times in self.symbols.items():
            result += '\n\t\t' + chr(symbol) + ' ' + str(times)

        result += '\n\n\t' + 'Words in file'

        for word, times in self.words.items():
            result += '\n\t\t' + word + ' ' + str(times)

        return result

    @staticmethod
    def get_all_counted_content():
        result = 'All symbols in all files'

        for symbol, times in all_symbols.items():
            result += '\n\t' + chr(symbol) + ' ' + str(times)

        result += '\n\nAll words in all files'

        for word, times in all_words.items():
            result += '\n\t' + word + ' ' + str(times)

        return result