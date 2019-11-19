import string
from random import choices

from rest_framework import serializers

from url_shortener.models import Link


class LinkSerializer(serializers.ModelSerializer):
	short_url = serializers.CharField(max_length=6, read_only=True)
	visits = serializers.IntegerField(read_only=True)
	created = serializers.DateTimeField(format='%H:%M:%S %d %b %Y', read_only=True)

	class Meta:
		model = Link
		fields = ('original_url', 'short_url', 'visits', 'created')

	def save(self, **kwargs):
		original_url = self.validated_data['original_url']
		short_url = self.encode_url()
		link = Link(original_url=original_url, short_url=short_url)
		link.save()
		return link

	def encode_url(self):
		characters = string.digits + string.ascii_letters
		short_url = ''.join(choices(characters, k=6))
		if Link.objects.filter(short_url=short_url).exists():
			return self.encode_url()
		return short_url
