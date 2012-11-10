import timeit

'''
The challenges featured in the script are:
Checking digits (#109, [Easy])
Scientific Notation (#108, [Easy])

'''

def check_digits(string, extras):
	'''
	From challenge #109 [Easy]
	Input: string of some kind
	Output: Truth value of whether all characters are digits
	'''
	# Make a list of digits to check membership
	digits = [str(x) for x in range(10)] + [extras]
	# Return the all() of truth values for membership
	# Could be made faster if we break when one zero is found
	return all([1 if x in digits else 0 for x in string])

def take_until_empty(stream1, filler=0, number=None):
	'''
	Take from stream one until exhausted, then take from stream 2
	If number is supplied, emit that many numbers

	Helper function for scientific notation
	'''
	
	index = 0
	for index, x in enumerate(stream1):
		if index > number:
			# If we have not exhausted the string by the time we hit the '.', 
			# yield the rest of the string and break
			yield '.'+stream1[index:]
			break
		# Yield numbers from stream1
		yield x

	# else pad with zeros until number is reached
	while index < number:
		index += 1
		yield filler

def scientific_notation():
	'''
	From challenge #108 [Easy]
	Given a number, convert to scientific notation
	Given a scientific notation, convert to digits

	This function takes either 'E' or 'x10^' labeled sci. notations
	It handles negative exponents correctly as well.
	'''

	def sci_to_digits(string):
		# See what the input switch is to break on
		switch = 'E' if 'E' in string else 'x10^'

		# Grab the goodies from the input string
		numbers, exponent = string.split(switch)
		number, mantissa = numbers.split('.')

		if int(exponent) > 0: 
			# Return the first number, then the padded mantissa or mantissa with a '.' added
			return ''.join([number, ''.join(take_until_empty(mantissa, '0', int(exponent)-1))])
		else:
			# If exponent is less than 0, we need to shift right.
			# Add 0. and pad with 0's until we run out of our exponent,
			# put the number and mantissa after
			return ''.join(['0.', str('0'*abs(int(exponent))), number, mantissa])

	def digits_to_sci(string, precision=3):
		# Convert to list so we can modify string
		l = list(string)

		# If there isn't a period in the string, we know we just have digits and a positive exponent
		if '.' not in string:
			# After the period we have [precision] many digits to include
			rem = l[1:precision+1]
			return ''.join([l[0], '.', ''.join(rem), 'E', str(len(string[1:]))])

		else:
			# If we do have a period, things get a little tougher
			if "0." in string[0:2]:

				char = '0'
				index = 1
				# See how many zeros after 0. we have
				while char == '0':
					index += 1
					char = string[index]
				# Our exponent is how many zeros we have (index)
				exponent = str(index-1)
				# Return the correctly formatted number (with given precision) and negated exponent
				return ''.join([string[index], '.', ''.join(l[index+1:index+1+precision]), 'E-', exponent])

	while True:

		string = raw_input("What number would you like to convert? > ")

		# A modified check digits that also checks for periods in string
		if check_digits(string, '.'):
			print digits_to_sci(string)

		else:
			print sci_to_digits(string.strip())


if __name__ == '__main__':
	scientific_notation()
