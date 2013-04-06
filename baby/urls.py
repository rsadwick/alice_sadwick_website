from django.conf.urls import patterns, url
from django.views.decorators.cache import cache_page
from views import get_article, index

urlpatterns = patterns('baby.views',
    url(r'^$', cache_page(60 * 5)(index)),
    url(r'^services/rsvp/$', 'rsvp'),
    url(r'^(?P<slug>[-\w]+)/$', cache_page(60 * 30)(get_article)),
    url(r'^services/instagram/$', 'get_instagram'),

)
