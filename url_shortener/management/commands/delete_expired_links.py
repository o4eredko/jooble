import pytz
from django.core.management.base import BaseCommand
from datetime import datetime, timedelta

from jooble import settings
from url_shortener.models import Link


class Command(BaseCommand):
	help = 'Delete objects older than 10 days'
	timezone = pytz.timezone(settings.TIME_ZONE)

	def is_expired(self, link):
		link.created = link.created.replace(tzinfo=self.timezone)
		to_delete = link.created <= datetime.now(self.timezone) - timedelta(days=link.lifetime)
		if to_delete:
			print(f"Link {link.id}: {link.original_url} deleted")
		return to_delete

	def handle(self, *args, **options):
		for link in filter(self.is_expired, Link.objects.all()):
			link.delete()
