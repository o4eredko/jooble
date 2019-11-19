from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from url_shortener.models import Link
from url_shortener.serializers import LinkSerializer
from url_shortener.utils import decode


class LinkViewSet(ModelViewSet):
	queryset = Link.objects.all()
	serializer_class = LinkSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]


def redirect_view(request, encoded_url):
	link = get_object_or_404(Link, id=decode(encoded_url))
	return HttpResponseRedirect(link.original_url)
