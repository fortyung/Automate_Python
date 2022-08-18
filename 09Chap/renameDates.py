#! python3
# renameDates.py - American-style dates (MM-DD-YYYY) in their names renamed 
# to European style dates (DD-MM-YYYY).

import re, os, shutil

patDate = re.compile(r'''^(.*?)		# StartWord --1 
	([0-1]?\d)-						# Month --2
	(([0-2]?\d)|(3[0-1]))-			# Day --3-4-5
	(\d{4})							# Year --6
	(.*?)$							# EndWord --7
	''', re.VERBOSE) 		

# lis_files = []

for file in os.listdir(os.getcwd()):
	if patDate.search(file) is not None:
		# lis_files.append(file)

		startWord = patDate.search(file).group(1)
		month = patDate.search(file).group(2)
		day = patDate.search(file).group(3)
		year = patDate.search(file).group(6)
		endWord = patDate.search(file).group(7)

		newName = startWord + day + '-' + month + '-' + year + endWord

		absPath = os.path.abspath('.')
		usaName = os.path.join(absPath, file)
		euName = os.path.join(absPath, newName)
		print('changing name from %s to %s' % (usaName, newName))
		# shutil.move(usaName, euName)