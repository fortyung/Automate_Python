#! python 3

import re
import sys

'''Regex Psattern'''
numRex = re.compile(r'[0-9]+')
lowerRex = re.compile(r'[a-z]+')
upperRex = re.compile(r'[A-Z]+')

if len(sys.argv) < 2:
    print('Usage: py nameOf_file.py [Password] -  account password')
    sys.exit()

'''Parameters'''
userspassword = sys.argv[1]
# print('Enter Password: ')
# userPass = input()



def passwordCheck(word):

	if len(word) < 8:
		print('Characters not up 8')
	elif numRex.search(word) is None:
		print('At least one digit')
	elif lowerRex.search(word) is None:
		print('At least one lowercase')
	elif upperRex.search(word) is None:
		print('At least one uppercase')	
	else:
		print('Strong Password!')

# passwordCheck(userPass)
passwordCheck(userspassword)
