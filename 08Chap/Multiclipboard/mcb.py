#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
# py.exe mcb.pyw list - Loads all keywords to clipboard.
# py.exe mcb.pyw delete <keyword> - deletes to keyword.
# py.exe mcb.pyw deleteAll - deletesAll to keyword.

import shelve, pyperclip, sys

mcbshef = shelve.open('mcb')

# Saves Keyword
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbshef[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 2:
	# Copies all the keywords 
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbshef.keys())))
	# Copies a particular Key
	elif sys.argv[1] in mcbshef:
		pyperclip.copy(mcbshef[sys.argv[1]])


if len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
	if sys.argv[2] in mcbshef:
		del mcbshef[sys.argv[2]]

elif sys.argv[1] == 'deleteAll':
	for key in mcbshef:
		del mcbshef[key]

mcbshef.close()