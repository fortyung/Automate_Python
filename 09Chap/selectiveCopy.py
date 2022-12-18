#! python3
# selectiveCopy.py: walks through a folder tree and searches for files with 
# a certain file extension (such as .pdf or .jpg). Copy these files from whatever 
# location they are in to a new folder.

import shutil, os

print(r'Enter Folder path: (eg.== C:\Users\path)')
folder = input()

print('Enter file extension to search: (eg. == .jpg, .py, .doc)')
extension = input()

print('Enter path destination: ')
destination = input()

for folderName, subfolders, filenames in os.walk(folder):
	print("Searching for %s in %s" % (extension, folderName))
	for file in filenames:
		if file.endswith(extension):
			source = os.path.join(folderName, file)
			shutil.copy(source, destination)
			# print(file)
