from django.urls import path, include
from rest_framework.routers import DefaultRouter

from url_shortener.views import LinkViewSet, redirect_view

router = DefaultRouter()
router.register('links', LinkViewSet)

urlpatterns = [
	path('', include(router.urls)),
	path('<slug:base62>', redirect_view, name='redirect-link')
]
