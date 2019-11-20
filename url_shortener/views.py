from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

from url_shortener.models import Link
from url_shortener.serializers import LinkSerializer
from url_shortener.utils import decode


@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'All links': reverse('link-list', request=request, format=format)
	})


class LinkListCreateApiView(ListCreateAPIView):
	queryset = Link.objects.all()
	serializer_class = LinkSerializer


class LinkDetailApiView(RetrieveAPIView):
	queryset = Link.objects.all()
	serializer_class = LinkSerializer


def redirect_view(request, encoded_url):
	try:
		link = get_object_or_404(Link, id=decode(encoded_url))
	except (ValueError, OverflowError):
		return HttpResponse(status=status.HTTP_404_NOT_FOUND)
	link.visits = link.visits + 1
	link.save()
	return HttpResponseRedirect(link.original_url)
