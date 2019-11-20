from django.urls import path, include

from url_shortener.views import redirect_view, index

urlpatterns = [
	path('', index, name='main-page'),
	path('api/', include('url_shortener.api.urls')),
	path('<encoded_url>', redirect_view, name='redirect-link')
]