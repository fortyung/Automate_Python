#! python3

# DelUnneeded.py :- program that walks through a folder tree and searches 
# for exceptionally large files  
import os

# print(r'Enter Folder path: (eg.== C:\Users\path)')
folder = input('Enter Folder path(eg.== C:\\Users\\path):\n')

numb = input('''Enter the maximum file size that you'd like to ignore (in megabytes): ''')


for folders, subfolders, filenames in os.walk(folder):
	for file in filenames:
		size = os.path.getsize(os.path.join(folders, file))  # Converting KB to MB
		if (size // 1000) >= int(numb): 
			print('File size is', size / 1000, 'MB and path is', os.path.join(folders, file))
