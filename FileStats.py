all_symbols = {}


# Stores file information
class FileStats(object):

    def __init__(self, file_name):
        self.symbols = {}
        self.file_name = file_name
        self.analyze_name()

    def analyze_name(self):
        for char in open(self.file_name).read():
            # for a file
            if not ord(char) in [9, 10, 32]:
                try:
                    self.symbols[ord(char)] += 1
                except KeyError:
                    self.symbols[ord(char)] = 1

                # for all files together
                try:
                    all_symbols[ord(char)] += 1
                except KeyError:
                    all_symbols[ord(char)] = 1

    def get_counted_symbols(self):
        result = self.file_name

        for symbol, times in self.symbols.items():
            result += '\n\t' + chr(symbol) + ' ' + str(times)

        return result

    @staticmethod
    def get_all_counted_symbols():
        result = 'All symbols in all files'

        for symbol, times in all_symbols.items():
            result += '\n\t' + chr(symbol) + ' ' + str(times)

        return result