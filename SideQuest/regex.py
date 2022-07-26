import re
sentence = 'Start a sentence and then bring it to an end'
pop = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( ) 
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
9005551234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
bat
cat
sat
pat
'''

pattern = re.compile(r'\d{3}-\d{3}-\d{4}')
# pattern = re.compile(r'start', re.IGNORECASE) # or re.I
# match = pattern.search(sentence)
# print(match)


# with open('text.txt', 'r') as f:
#     content = f.read()

#     match = pattern.finditer(content)
#     f.seek(8000)
#     for items in match:
#         print(items)

with open('text.txt', 'r') as f:
	content = f.read()

	match = pattern.finditer(content)
	for items in match:
		print(items)