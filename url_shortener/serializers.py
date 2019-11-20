from django.contrib.sites.shortcuts import get_current_site
from rest_framework import serializers

from url_shortener.models import Link
from url_shortener.utils import encode


class LinkSerializer(serializers.HyperlinkedModelSerializer):
	short_url = serializers.SerializerMethodField(read_only=True)
	visits = serializers.IntegerField(read_only=True)
	created = serializers.DateTimeField(format='%H:%M:%S %d %b %Y', read_only=True)
	lifetime = serializers.IntegerField(min_value=1, max_value=360, default=90)

	class Meta:
		model = Link
		fields = ('url', 'short_url', 'original_url', 'visits', 'created', 'lifetime')

	def get_short_url(self, obj):
		url = get_current_site(self.context.get('request')).domain
		return f"{url}/{encode(obj.id)}"
