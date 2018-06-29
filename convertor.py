#coding=utf-8
from PIL import Image
import os
from os import listdir
from os.path import isfile, join

input_path = 'webp'
output_path = 'jpg'

# Get a list of all file names

folder_id = 1
for sub_folder_path in listdir(input_path):
    print('Working on folder: ' + sub_folder_path)
    print('EP: ' + str(folder_id) + '/' + str(len(listdir(input_path))))
    os.mkdir(output_path + '/' + sub_folder_path);

    file_id = 1
    for files in listdir(input_path + '/' + sub_folder_path):
        im = Image.open(input_path + '/' + sub_folder_path + '/' + files).convert("RGB")
        im.save((output_path + '/' + sub_folder_path + '/' + files).replace('.webp','.jpg'), "jpeg")

        print('Page: ' + str(file_id) + '/' + str(len(listdir(input_path + '/' + sub_folder_path))))
        file_id += 1

    folder_id += 1

print('Done.')

key = input('Press any key to quit')
quit()
