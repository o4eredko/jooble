from django.urls import path

from url_shortener.views import *


urlpatterns = [
	path('links/', LinkListCreateApiView.as_view(), name='link-list'),
	path('<encoded_url>', redirect_view, name='redirect-link')
]
