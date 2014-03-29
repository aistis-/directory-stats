import sys
from os import listdir
from os.path import isfile, join
import FileStats

directory = sys.argv[1]

files = [f for f in listdir(directory) if isfile(join(directory, f))]

all_files_names = ''

for i, file in enumerate(files):
    all_files_names += ' ' + file
    files[i] = FileStats.FileStats(file)

string_to_file = ''

for file in files:
    string_to_file += file.get_counted_symbols()

with open(sys.argv[2], 'w') as output:
    output.write(string_to_file)


