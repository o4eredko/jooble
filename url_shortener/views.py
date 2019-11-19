from rest_framework.generics import ListCreateAPIView

from url_shortener.models import Link
from url_shortener.serializers import LinkSerializer


class LinkListApiView(ListCreateAPIView):
	queryset = Link.objects.all()
	serializer_class = LinkSerializer
