#! python3
# fillGap.py: a program that finds all files with a given prefix

import re, os

folder = input('Enter Folder path(eg.== C:\\Users\\path):\n')

prefix = input('Enter the prefix:\n')

pattern = re.compile(r'(%s)(\d*)(\..*)' % (prefix))

listF = []

for folderName, subfolders, filenames in os.walk(folder):
	for files in filenames:
		if pattern.search(files) is not None:

			length = len(pattern.search(files).group(2))

			extension = pattern.search(files).group(3)

			listF.append(pattern.search(files).group(2))

	ordered = sort([int(i) for i in listF])

for num in range(1, len(listF) + 1):

	zeroes = '0' * (length - len(str(num)))

	new_path = '{}/{}{}{}'.format(folder, prefix, zeroes, num, extension)



