import numbers

BASE62_DIGITS = 'rdOsQ8oHtnLWGk0fIFzc1iXY2EPaR9bMZ4qpAKlyuSxmeVh5v7JjU3gC6DBNwT'


def encode(num):
	if not isinstance(num, numbers.Real) or num < 0:
		raise ValueError("num parameter must be an integer greater than zero")
	if num == 0:
		return str(BASE62_DIGITS[0])
	res = []
	while num:
		remainder = num % 62
		num = num // 62
		res.append(BASE62_DIGITS[remainder])
	return ''.join(reversed(res))


def decode(encoded_str):
	if not isinstance(encoded_str, str):
		raise ValueError("num parameter must be a string in base62 format")
	res = 0
	for symbol in encoded_str:
		res = 62 * res + BASE62_DIGITS.find(symbol)
	return res
