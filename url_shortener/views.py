from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import status

from url_shortener.models import Link
from url_shortener.utils import decode


def index(request):
	return render(request, template_name='index.html')


def redirect_view(request, encoded_url):
	try:
		link = get_object_or_404(Link, id=decode(encoded_url))
	except (ValueError, OverflowError):
		return HttpResponse(status=status.HTTP_404_NOT_FOUND)
	link.visits = link.visits + 1
	link.save()
	return HttpResponseRedirect(link.original_url)
