import os
import shutil
import datetime

current_date = datetime.datetime.now()
day = str(current_date.day)
month = str(current_date.month)
year = str(current_date.year)


cwd = os.getcwd()


origin_folder = open(fr"{cwd}/origen.txt", "r")
origin = origin_folder.readline()

destination_folder = open(fr"{cwd}/destino.txt", "r")
half_destination = destination_folder.readline()


destination = fr'{half_destination}{year}\{month}\{year}-{month}-{day}'

try:
    os.mkdir(f'{half_destination}{year}')
except FileExistsError as erro:
    pass

try:
    os.mkdir(f'{half_destination}{year}/{month}')
except FileExistsError as erro:
    pass

try:
    os.mkdir(destination)
except FileExistsError as erro:
    pass

for root, dirs, files in os.walk(origin):
    for file in files:
        old_file_path = os.path.join(root, file)
        new_file_path = os.path.join(destination, file)
        shutil.move(old_file_path, new_file_path)