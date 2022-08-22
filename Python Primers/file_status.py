import os

# print contents of current directory
print(os.listdir())

# print all files
print([o for o in os.listdir() if os.path.isfile(o)])

# print all directory
print([o for o in os.listdir() if os.path.isdir(o)])

# get all python files
import glob
print(glob.glob('*.py'))


# sort all files in alphabetical order
files = [o for o in os.listdir() if os.path.isfile(o)]
print(sorted(files, key = str.lower))

# sort all files by their file size (largest first)
print(sorted(files, key=lambda x:os.stat(x).st_size, reverse = True))

#  get 1 largest files in the directory use heapq
import heapq
largest = heapq.nlargest(2, files, key = lambda x: os.stat(x).st_size)
print(largest)

# zip the 2 largest files into 'largest.zip' file
from  zipfile import ZipFile


with ZipFile('largeest.zip','w') as zip_file:
    for f in largest:
        zip_file.write(f)