from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'alice.views.home', name='home'),
    # url(r'^alice/', include('alice.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', include('baby.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^baby/', include('baby.urls')),
    url(r'^template/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
    url(r'^services/rsvp/$', 'rsvp'),
)
