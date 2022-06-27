# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

# #! python 3
#uncomment to execute


import pyperclip

text = pyperclip.paste()

line = text.split('\n')

for i in range(len(line)):
	line[i] = '*' + line[i]

text = '\n'.join(line)

pyperclip.copy(text)
