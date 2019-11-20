from django.urls import path

from url_shortener.api.views import LinkListCreateApiView, LinkDetailApiView, api_root


urlpatterns = [
	path('', api_root, name='api-root'),
	path('links/', LinkListCreateApiView.as_view(), name='link-list'),
	path('links/<int:pk>', LinkDetailApiView.as_view(), name='link-detail'),
]
