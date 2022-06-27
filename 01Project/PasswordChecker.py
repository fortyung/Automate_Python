#Password verification

# #! python 3
#uncomment to execute

import sys, pyperclip #pyperclip is a module for copying and pasting

PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
 'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
 'luggage': '12345'}	#Dictionary of data


if len(sys.argv) < 2:
	print('Usage: py pw.py [account] - copy account password')
	sys.exit()

account = sys.argv[1] # account name

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for ' + account + ' copied to clipboard.')
else:
 print('There is no account named ' + account)