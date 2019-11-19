from django.db import models


class Link(models.Model):
	original_url = models.CharField(max_length=512, unique=True)
	short_url = models.CharField(max_length=6)
	visits = models.IntegerField(default=0)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.short_url
