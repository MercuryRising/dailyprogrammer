import re

def strip_c_comments(fp):
	with open(fp, 'rb') as f:
		data = f.read()	

	comments =	re.findall(r'(//.*?\n)|(/\*.*?\*/)|(".*?(?<!\\)")', data)

	comm = [rex  for comment in comments for index, rex in enumerate(comment) if (rex != ''  and index != 2)]
	for c in comm:
		if c[-1] == '\n':
			c = c[:-1]
		data = data.replace(c, '') 

	minName, ext = fp.split('.')
	newPath = ''.join([minName, '.min.', ext])
	with open(newPath, 'wb') as f:
		f.write(data)

	return data

strip_c_comments('example.c')


