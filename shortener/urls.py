__author__ = 'nikoladang'
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    # for our home/index page

    # url(r'^articles/(?P<year>[0-9]{4})/$', views.redirect_original),
    ##url(r'^(?P<year>aaaa)/', views.redirect_original),
    url(r'^(?P<short_id>[a-zA-Z0-9]+)/', views.redirect_original),
    # url(r'^(?P<short_id>[0-9]+)/$', views.redirect_original, name='redirectoriginal'),
    # url(r'^(?P<short>\w+)/$', views.redirect_original, name='redirectoriginal'),
    #url(r'^\w+/$', views.redirect_original, name='redirectoriginal'),
    #url(r'^(?P<short>\w+)/$', views.redirect_original, name='redirectoriginal'),
    # url(r'^[0-9]{2}/$', views.redirect_original, name='redirectoriginal'),
    # url(r'^aa/$', views.redirect_original, name='redirectoriginal'),
    # when short URL is requested it redirects to original URL

    # url(r'^makeshort/$', views.shorten_url, name='shortenurl'),
    # this will create a URL's short id and return the short URL
]