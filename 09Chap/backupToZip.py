#! python3
#Usage: backupTozip.py - function that Backs up a Folder into a ZIP File

import zipfile, os
def backupTozip(folder):

	folder = os.path.abspath(folder)
	num = 1
	while True:
		zipName = os.path.basename(folder) + '_%s.zip' % (num)
		print('creating...%s' % (zipName))

		if os.path.exists(zipName) is False:
			break
		num += 1


	newZip = zipfile.ZipFile(zipName, 'w')

	for folderName, subfolders, filenames in os.walk(folder):
		print('adding files in %s...' % (folderName))
		newZip.write(folderName)
		for files in filenames:
			if files.startswith(os.path.basename(folder) + '_') and files.endswith('.zip'):
				continue
			newZip.write(os.path.join(folderName, files))
	newZip.close()

# backupTozip(r'C:\Users\HP\Automate_python\07Chap')
u = input()
backupTozip(u)