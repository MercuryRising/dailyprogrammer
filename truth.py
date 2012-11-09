import re

def algebra(instring):
	print '\nInput: ', instring	
	parentheses = []
	values = re.findall(r'\(([A-Z]) (\b\w\w+\b) ([A-Z])\)|(\b\w\w+\b)|([A-Z])', instring)
	values = [[x for x in y if x != ''] for y in values]
	
	variables = list(set([x for y in values for x in y if x in 'ABCD']))
	#print "Variables used: ", variables

	niceString = []
	parentheses = []
	parseThis = []

	for x in values:
		if len(x) > 1:
			niceString.append('('+' '.join(x)+')')
			parentheses.append(x)
		else:
			niceString.append(x[0])

	parseThis = niceString
	print ' '.join(niceString)

	def printalg(value, ans):
		#print value
		nn = ' '.join(niceString)

		for var in variables:
			nn = nn.replace(var, str(lookup[var]))
		print nn, '=', 1 if ans == True else 0

	def operate(value):
		first = lookup[value[0]]
		second = lookup[value[2]]
		operator = value[1]
		if operator == 'and':
			return (first and second)
		elif operator == 'or':
			return (first or second)
		elif operator == 'nand':
			return not (first & second)
		elif operator == 'nor':
			return not (first or second)

	def parseIt(data):
		if len(parentheses) > 0:
			for index, value in enumerate(parentheses):
				if type(value) == list:
					ans = operate(value)
					#printalg(value, ans)
					lookup["("+' '.join(value) + ")"] = ans				
		ans = operate(data)
		printalg(data, ans)

	#print 'Parentheses: ', parentheses

	lookup = {0:0, 1:1}
	for var in variables:
		lookup[var] = 0

	for x in range(len(variables)**2):
		nv = [x&1, (x&2)>>1, (x&4)>>2, (x&8)>>3]
		nv = nv[:len(variables)][::-1]

		for index, var in enumerate(variables):
			lookup[var] = nv[index]
		
		parseIt(parseThis)

algebra('A nor B')
algebra('C and (B and D)')
algebra('A nand C nor A nor D')
algebra('A nor D')
