"""
Project's URL Configuration
"""
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
import django.contrib.auth.urls as auth_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(auth_urls)),
    url(r'', include('simte.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
