#! python3
'''madLib.py is a program that reads in text files and lets the user add 
their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
appears in the text file.'''
import re

mad_lib = open('mad.txt', 'w')
mad_lib.write('''The ADJECTIVE panda walked to the NOUN and 
then VERB. A nearby NOUN was unaffected by these events.''')
mad_lib.close()

pattern = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')

mad_lib = open('mad.txt', 'r')
content = mad_lib.read()
mad_lib.close()

while True:
	matches = pattern.search(content)

	if  matches == None:
		break
	elif matches.group() ==  'ADJECTIVE' or matches.group() == 'ADVERB':
		print('Enter an %s:' % (matches.group().lower()))
	elif matches.group() ==  'NOUN' or matches.group() == 'VERB':
		print('Enter an %s:' % (matches.group().lower()))
	data = input()

	content = pattern.sub(data, content, 1)

print(content)
print('Name your file:')
newFile = input()
new_file = open('.\\%s.txt' % (newFile), 'w')
new_file.write(content)
new_file.close()