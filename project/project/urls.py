
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from project.settings import STATICFILES_DIRS
urlpatterns = patterns('',
    # Examples:
    url(r'^[/]?$', 'mupload.views.index', name='mupload'),
    url(r'^upload/$', 'mupload.views.upload'),
    url(r'^jupload/$','mupload.views.jupload'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    (r'^site_media/(?P<path>.*)$','django.views.static.serve',
        {'document_root':STATICFILES_DIRS,'show_indexes': True}),
)
