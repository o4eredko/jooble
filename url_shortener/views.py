from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from url_shortener.models import Link
from url_shortener.serializers import LinkSerializer
from url_shortener.utils import decode, encode


class LinkListCreateApiView(ListCreateAPIView):
	queryset = Link.objects.all()
	serializer_class = LinkSerializer

	def create(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		url = serializer.validated_data['original_url']
		links = Link.objects.filter(original_url=url)
		if links.exists():
			serializer = self.get_serializer(links[0])
			return Response(serializer.data, status=status.HTTP_200_OK)
		self.perform_create(serializer)
		headers = self.get_success_headers(serializer.data)
		return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


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
