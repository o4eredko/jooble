from django.db import models


class Link(models.Model):
	original_url = models.CharField(max_length=512, unique=True)
	visits = models.IntegerField(default=0)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.original_url
