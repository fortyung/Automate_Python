#! python3
import re, pyperclip

phoneRex = re.compile(r'''(
	(\d{3}|\(\d{3}\))					# area code
	(\s|-|.)?							# separator
	(\d{3})								# first 3 digits
	(\s|-|\.)							# separator
 	(\d{4}) 							# last 4 digits
 	(\s*(ext|x|ext.)\s*(\d{2,5}))? 		# extension
	)''', re.VERBOSE)

emailRex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+	# uersname
	@					# @
	[a-zA-z.-]+			# domain name
	(\.[a-zA-Z]{2,4})	# dot-something
	)''', re.VERBOSE)	# 

text = str(pyperclip.paste())

matches = []

for groups in phoneRex.findall(text):
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	if groups[8] != '':
		phoneNum += ' x' + groups[8]
	matches.append(phoneNum)

for groups in emailRex.findall(text):
	matches.append(groups[0])

if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard')
	print('\n'.join(matches))
else:
	print('No phone numbers or emails found')





