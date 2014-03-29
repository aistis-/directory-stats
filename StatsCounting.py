import sys
from os import listdir
from os.path import isfile, join
import FileStats

directory = sys.argv[1]

files = [f for f in listdir(directory) if isfile(join(directory, f))]

files_stats = [FileStats.FileStats(file) for file in files]

string_to_file = ''

for file in files_stats:
    string_to_file += file.get_counted_symbols() + '\n\n'

string_to_file = FileStats.FileStats.get_all_counted_symbols() + '\n\n' + \
    string_to_file

with open(sys.argv[2], 'w+') as output:
    output.write(string_to_file)
