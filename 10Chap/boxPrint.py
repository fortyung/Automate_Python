'''
Testing Debugging.
'''
#! python3

def boxprint(symbol, width, height):
	if len(symbol) != 1:
		raise Exception('Symobl must be a single charactter string.')
	if width <= 2:
		raise Exception('width must be greater than 2.')
	if height <= 2: 
		raise Exception('height must be greater than 2.')
	print(symbol * width)

	for i in range(height - 2):
		print(symbol + (' ' * (width - 2)) + symbol)
	print(symbol * width)

for sym, w, h in (('*',4,4), ('O',20,5), ('x',1,3), ('ZZ',3,2),):
	try:
		boxprint(sym,w,h)
	except Exception as err:
		print('An Exceptionhappened: ' + str(err))
