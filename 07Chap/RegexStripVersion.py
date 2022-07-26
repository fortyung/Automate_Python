import re
'''Regex Version of the strip Func'''
def restrip(word, remove=''):

	if remove == '':
		'''Removes white spaces'''
		left_p = re.compile(r'^\s*')
		right_p = re.compile(r'\s*$')

		word = left_p.sub('', word)
		word = right_p.sub('', word)

		return word
	else:
		'''Removes specified keywords'''
		lef_p = re.compile(r'^([%s]+)' % remove)
		ref_p = re.compile(r'([%s]+)$' % remove)

		word = lef_p.sub('', word)
		word = ref_p.sub('', word)

		return word
print(restrip('   goo  ood  '))
print(restrip('nnnnmansnnn', 'n'))
