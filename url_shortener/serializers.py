from rest_framework import serializers

from url_shortener.models import Link
from url_shortener.utils import encode


class LinkSerializer(serializers.HyperlinkedModelSerializer):
	short_url = serializers.SerializerMethodField(read_only=True)
	visits = serializers.IntegerField(read_only=True)
	created = serializers.DateTimeField(format='%H:%M:%S %d %b %Y', read_only=True)

	class Meta:
		model = Link
		fields = ('id', 'url', 'original_url', 'short_url', 'visits', 'created')

	def get_short_url(self, obj):
		url = self.context.get('request').get_full_path()
		return url + encode(obj.id)

	def save(self, **kwargs):
		original_url = self.validated_data['original_url']
		link = Link(original_url=original_url)
		link.save()
		return link
