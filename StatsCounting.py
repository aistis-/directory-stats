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

