from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .settings import BASE_URL


urlpatterns = [
    path('admin/', admin.site.urls),
    path(BASE_URL, include('api.urls')),
    # swagger ui docs
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'docs/',
        SpectacularSwaggerView.as_view(
            template_name='swagger-ui.html',
            url_name='schema'
        ),
        name='swagger-ui'
    )
]
