from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

from url_shortener.models import Link
from url_shortener.api.serializers import LinkSerializer


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
