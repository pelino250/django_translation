"""
URL configuration for django_translation project.

URLs are organized into two groups:
1. Non-localized URLs (in urlpatterns)
2. Localized URLs (in i18n_patterns)

For more information on URL configuration, see:
https://docs.djangoproject.com/en/5.0/topics/http/urls/
"""
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.urls.resolvers import URLPattern, URLResolver
from typing import List, Union

from core import views

# Non-localized URLs
urlpatterns: List[Union[URLPattern, URLResolver]] = [
    # Language selection URL
    path('i18n/', include('django.conf.urls.i18n')),
]

# Localized URLs
# These URLs will be prefixed with the language code (e.g., /en/blog/, /fr/blog/)
urlpatterns += i18n_patterns(
    # Admin interface
    path('admin/', admin.site.urls),

    # Blog URLs
    path('blog/', views.posts, name='blog'),

    # Home page
    path('', views.index, name='index'),

    # Don't prefix the default language
    prefix_default_language=False
)
