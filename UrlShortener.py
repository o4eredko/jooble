import string


class UrlShorten:
	id = 100
	encoded_urls = {}
	digits = string.digits + string.ascii_lowercase + string.ascii_uppercase

	def shorten_url(self, original_url):
		if original_url in self.encoded_urls:
			id = self.encoded_urls[original_url]
			shorten_url = self.encode(id)
		else:
			self.encoded_urls[original_url] = self.id
			shorten_url = self.encode(self.id)
			self.id += 1
		return f'127.0.0.1:5000/{shorten_url}'

	def encode(self, num):
		base = len(self.digits)
		res = []
		while num:
			idx = num % base
			res.append(self.digits[idx])
			num //= base
		return ''.join(reversed(res))
