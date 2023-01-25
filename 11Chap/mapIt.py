'''
mapIt.py - Launches a map in the browser using an address from the
command line or clipboard.
'''
#! python3

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    #get address from command line
    ADDRESS = ' '.join(sys.argv[1:])
else:
    #get address from clipboard
    ADDRESS = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + ADDRESS)
