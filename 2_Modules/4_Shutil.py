#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
#! /library/Frameworks/Python.framework/Versions/3.5/python3.5
# ===================================================================================================
# +++++++++ Shutil module +++++++++
# shutil.copy(source, destination) - copy file from source to destination
#                                  - source an destination are strings
#                                  - destination can be either a path or a new file name (with path)
# shitil.copytree(source, destination) - copy all the files and subfolders from source to destination
# shutil.move(source, destination) - if source is folder, the file gets moved
#                                  - if there is file in destination, it will be overwritten
#                                  - if destination is file name, file will be moved and renamed
#                                  - destination folder must exist for move() to work properly
# os.unlink(path) - will delete one file at path
# os.rmdir(path) - will remove one folder at path; folder must be empty
# shutil.rmtree(path) - will remove folder with its contents
# you can also use 3rd party send2trash module to safely delete files
# send2trash.send2trash('filename') - places file into the trash bin
# os.walk(path) - walks over folder, subfolders and all files within those folder
#               - you need to path the string, folder where you want to explore contents
#               - retunrns: string of current folder name, list of folders in the current folder, list of filenames
# zipfile - allows to work with zip files; you can create and open zip files
#         - first you import zipfile
#         - file = zipfile.ZipFile('filename.zip') - create zip object
#         - file.extractall(path where to extract) - can extract files, path is optional
#         - file.close() - close the object
#         - file.extract(what to extract, where to extract) will extract single file that you define

# in this exmple we will delete all files with txt extension
import os
for filename in os.listdir():
    if filename.endswith('.txt'):
        # os.unlink(filename)
        print('Deleted ', filename)

# in this example we will use send2trash module
import send2trash
baconfile = open('bacon.txt', 'w')
baconfile.write('Hello')
baconfile.close()
send2trash.send2trash('bacon.txt')

# in the example we will use os.walk()
for folder_name, subfolders, filenames in os.walk('/Users/nikolay.poturnak/PycharmProjects/Python_practice/'):
    print('The current folder is: ', folder_name)
    for subfolder in subfolders:
        print('\tSubfolder is: ', subfolder)
    for filename in filenames:
        print('\t\tInclufed file is: ', filename)

# in this example we will work with zip module
import zipfile
fileZip = zipfile.ZipFile('Hello.txt.zip')
print(fileZip.namelist())
print(fileZip.getinfo('Hello.txt'))
fileZip.extractall()
fileZip.close()

# creating a zip file
# import zipfile
# newZip = zipfile.ZipFile('new.zip', 'w') - this will add one file to zip, use 'a' if you need to be adding to zip
# newZip.write('spam.txt', compress_typ=zipfile.ZIP_DEFLATED)
# newZip.close()