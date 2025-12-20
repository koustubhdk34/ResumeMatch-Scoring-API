from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import home

# Swagger imports
if settings.DEBUG:
    from rest_framework import permissions
    from drf_yasg.views import get_schema_view
    from drf_yasg import openapi

    schema_view = get_schema_view(
        openapi.Info(
            title="JobTrack API",
            default_version='v1',
            description="Backend API for Resume Matching & Job Application Tracking",
            contact=openapi.Contact(email="youremail@example.com"),
        ),
        public=True,
        permission_classes=[permissions.AllowAny],
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('api/auth/', include('accounts.urls')),
    path('api/resumes/', include('resumes.urls')),
    path('api/applications/', include('applications.urls')),
]

# Only include Swagger/Redoc in DEBUG mode
if settings.DEBUG:
    urlpatterns += [
        path('swagger(<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
