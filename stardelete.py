import re

def non_regex(test):
	print 'Before (nrx): ', test

	stars = [index for index, char in enumerate(test) if char == '*']

	for ind in stars:
		left = ind-1 if (ind-1 >= 0 and test[ind-1] != '*') else -1
		right = ind+1 if (ind+1 < len(test) and test[ind+1] != '*') else -1

		indices = [left, right, ind]

		for ind in set(indices)-set([-1]):
			test[ind] = '-'

	test = ''.join([x for x in test if x != '-'])
	print 'After (nrx): ', test, '\n'

def regex(test):
	print 'Before (rx): ', test

	test = re.sub(".?\*+.?", '', test)
	# [a-z]\*[a-z])|([a-z]\*)|(\*[a-z])
	print 'After (rx): ', test, '\n'

tests = ["adf*lp", "a*o", "*dech*", "de**po", "sa*n*ti", "abc"]

for test in tests:
	regex(test)

tests = [list(t) for t in tests]

for test in tests:
	non_regex(test)


