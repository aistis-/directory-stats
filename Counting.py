import sys
from os import listdir
from os.path import isfile, join
import FileStats

directory = sys.argv[1]

files = [f for f in listdir(directory) if isfile(join(directory, f))]

files_stats = [FileStats.FileStats(file) for file in files]

output_string = ''

for file in files_stats:
    output_string += file.get_counted_content() + '\n\n'

output_string = FileStats.FileStats.get_all_counted_content() + '\n\n' + \
    output_string

with open(sys.argv[2], 'w+') as output:
    output.write(output_string)
