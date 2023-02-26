
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Starwars Local API in python.",
      default_version='v1',
      description="""Welcome to the swapi, the Star Wars API! 
      This documentation should help you familiarise yourself with the resources available and how to consume
        them with HTTP requests. If you're after a native helper library then I suggest you scroll 
        down and check out what's available. Read through the getting started section before you dive in. 
        Most of your problems should be solved just by reading through it.""",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="dimbisoapatrick@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('backend.starwarstasks.urls')),
    #
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
