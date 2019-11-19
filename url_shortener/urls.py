from django.urls import path

from url_shortener.views import LinkListApiView

urlpatterns = [
	path('links/', LinkListApiView.as_view(), name='link-list')
]
