from __future__ import absolute_import, unicode_literals

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from search import views as search_views
from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtailcore import urls as wagtail_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls

from wagtail.contrib.wagtailapi import urls as wagtailapi_urls
from wagtail.contrib.wagtailsitemaps.views import sitemap

from shortener import views as shortener_views

urlpatterns = [
    # url(r'^s/', include('shortener.urls')),

    # url(r'^googlee61d09ae5cc87100\.html', shortener_views.draft),

    url(r'^django-admin/', include(admin.site.urls)),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', search_views.search, name='search'),
    url('^sitemap\.xml$', sitemap),

    url(r'^s/', include('shortener.urls')),

    # url(r'^s/', include('shortener.urls',
    #     namespace='shortener')),

    url(r'^api/', include(wagtailapi_urls)),
    # url(r'^iprestrict/', include('iprestrict.urls', namespace='iprestrict')),

    url(r'', include(wagtail_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # my custom
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)