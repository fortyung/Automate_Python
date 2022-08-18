#! python3
# regexSearch.py - opens all .txt files in a folder and searches for any 
# line that matches a user-supplied regular expression.
import re, os

lis_files = []
for file in os.listdir(os.getcwd()):
	if file.endswith('.txt'):
		lis_files.append(file)

'''The code below can replace the entire code above'''

'''# Finds all the '.txt' files in the current dir
	files_txt = ' '.join(os.listdir(os.getcwd()))

	# The pattern for the '.txt' file
	pattern = re.compile(r'\w+(.txt)')
	matches =  pattern.finditer(files_txt)

	#list for the files
	lis_files = []

	for i in matches:
		s = i.start()
		e = i.end()
		lis_files.append(files_txt[s:e])'''

print('Enter word to search:')
word = input()

# Opening the files 
for file in lis_files:
	doc = open('%s' % (file), 'r')
	content = doc.read()
	doc.close()

	# Searches the files for keyword
	result = re.search(word, content) 

	if result == None:
		continue
	else:
		print('found in %s: %s' % (file, result.group()))