from django.test import TestCase
from rest_framework import status
from rest_framework.reverse import reverse


class LinkTestCase(TestCase):
	add_link_url = reverse('link-list')

	def setUp(self) -> None:
		pass

	def test_link_add_valid(self):
		default_lifetime = 90
		data = {
			'original_url': 'https://ua.jooble.org/'
		}
		response = self.client.post(self.add_link_url, data=data)
		self.assertEquals(response.status_code, status.HTTP_201_CREATED)
		self.assertEquals(response.data['lifetime'], default_lifetime)

	def test_link_error_invalid_lifetime(self):
		data = {
			'original_url': 'https://ua.jooble.org/',
			'lifetime': 0
		}
		response = self.client.post(self.add_link_url, data=data)
		self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
		data['lifetime'] = 361
		response = self.client.post(self.add_link_url, data=data)
		self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

	def test_link_error_invalid_url(self):
		data = {
			'original_url': 'https://'
		}
		response = self.client.post(self.add_link_url, data=data)
		self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
		data['original_url'] = 'https://jooble/'
		response = self.client.post(self.add_link_url, data=data)
		self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
