'''with open('text.txt', 'r') as rf:
	with open('text_copy.txt', 'w') as wf:
		for line in rf:
			wf.write(line)
'''
with open('nkn.jpg', 'br') as rf:
	with open('pic_copy.jpg', 'bw') as wf:
		size = 4096
		chunk = rf.read(size)

		while len(chunk) > 0:
			wf.write(chunk)
			chunk = rf.read(size)