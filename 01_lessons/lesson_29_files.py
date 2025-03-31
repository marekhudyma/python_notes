# f = open('/tmp/practice.txt', 'w+')
# f.write('This is a test string')
# f.close()
import os
# import os
# print(os.getcwd())
# print(os.listdir())
#
# print(os.listdir("/tmp"))
#
# import shutil
# shutil.move('/tmp/practice.txt', '/tmp/practice2.txt')

# os.unlink('/tmp/practice2.txt') # removes file
# os.rmdir('/tmp/subdir') # removes dir if empty
# shutil.rmtree('/tmp/subdir') # removes all files and folders in path !!!

# pip install send2trash
# installed in PyCharm

# import send2trash
# send2trash.send2trash("/tmp/practice.txt")

for folder, sub_folders, files in os.walk('.'):
    print(f'Currently looking at {folder}')
    print('\n')
    print('The subfolders are:')
    for sub_folder in sub_folders:
        print(sub_folder)
    print('\n')
    print('The files are:')
    for file in files:
        print(f'File: {file}')
    print('\n')