import string


def to_base62(num, b=62):
	if b <= 0 or b > 62:
		return 0
	base = string.digits + string.ascii_lowercase + string.ascii_uppercase
	r = num % b
	res = base[r]
	q = num // b
	while q:
		r = q % b
		q = q // b
		res = base[int(r)] + res
	return res


def to_base10(num, b=62):
	base = string.digits + string.ascii_lowercase + string.ascii_uppercase
	limit = len(num)
	res = 0
	for i in range(limit):
		res = b * res + base.find(num[i])
	return res
