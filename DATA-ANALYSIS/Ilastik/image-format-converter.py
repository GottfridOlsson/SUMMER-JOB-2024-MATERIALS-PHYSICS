##=====================================================##
##        File: image-format-converter.py
##      Author: GOTTFRID OLSSON 
##     Created: 2023-08-08
##     Updated: 2024-06-28
##       About: Takes a rootpath and converts all files
##              with specified extensions into files
##              with new extension in all sub-
##              directories from rootpath.
##=====================================================##

from PIL import Image
import os



# CHANGE THESE FOR YOUR CASE #
rootpath_for_conversion = 'C:\\SUMMER-JOB-2024-MATERIALS-PHYSICS\\DATA-ANALYSIS\\Ilastik\\Training images\\.tif\\' # remember to write '\\' for every '\'
current_extensions = ['.tif'] # read about file formats: https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html
new_extension = '.tiff'
convert = True
remove_old_files = False




def get_absolute_path_of_directories_and_files_in_rootpath(rootpath):
    # brrowed from: https://stackoverflow.com/questions/120656/directory-tree-listing-in-python?noredirect=1&lq=1
    directories_path, files_path = [], []

    for dirname, dirnames, filenames in os.walk(rootpath_for_conversion):
        
        for subdirname in dirnames:
            directories_path.append(os.path.join(dirname, subdirname))
        
        for filename in filenames:
            files_path.append(os.path.join(dirname, filename))

    return directories_path, files_path



if convert == True:

    print(f'\nBeginning file conversion in rootpath {rootpath_for_conversion}.')
    print(f'Files with extensions {current_extensions} will be created with new extension \'{new_extension}\'.')
    if not remove_old_files: not_string = 'NOT '
    else: not_string = ''
    print(f'Old files will ' + not_string + 'be deleted!')
    answer = input('Continue? (Y/N): ')

    if answer.lower() in ['y', 'yes']:

        _, file_paths = get_absolute_path_of_directories_and_files_in_rootpath(rootpath_for_conversion)

        for file_path in file_paths:

            image_path, image_extension = os.path.splitext(file_path)

            if image_extension in current_extensions:

                image = Image.open(file_path)

                if new_extension in ['.jpg', '.jpeg']:
                    rgb_image = image.convert('RGB')
                    rgb_image.save(image_path + new_extension)
                else:
                    image.save(image_path + new_extension)

                image.close()   
                print(f'CREATED: {file_path} was created.')
                
                if remove_old_files:
                    os.remove(file_path)
                    print(f'DELETED: {file_path} was deleted.')
            else: 
                print(f'UNCHANGED: {file_path} was unchanged.')

    elif answer.lower() in ['n', 'no']:
        print('Procedure aborted.')
    else:
        print("Procedure aborted due to bad user input, please answer 'Y' or 'N' next time.")






'''
# REMOVE OLD FILES, fail-safe
_, converted_file_paths = get_absolute_path_of_directories_and_files_from_rootpath(rootpath_for_conversion)

old_extensions = current_extensions

if False:
    print(f'\nBeginning removal of old files in rootpath {rootpath_for_conversion}:')

    for converted_file_path in converted_file_paths:
        _, image_extension = os.path.splitext(converted_file_path)

        if image_extension in old_extensions:
            os.remove(converted_file_path)
            print(f"REMOVED: {converted_file_path}")

    print('\n')
'''