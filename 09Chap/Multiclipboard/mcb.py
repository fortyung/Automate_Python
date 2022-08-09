#! python3
# mcb.pyw -  Saves and loads pieces of text to the clipboard
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword
# py.exe mcb.pyw <keyword> - Loads keyword to clipboard
# py.exe mcb.pyw list - Loads all keywords to clipboard
import sys, pyperclip, shelve

mcbshef = shelve.open('mcb')

if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbshef[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbshef.keys())))
    elif sys.argv[1] in mcbshef:
        pyperclip.copy(mcbshef[sys.argv[1]])
mcbshef.close()

