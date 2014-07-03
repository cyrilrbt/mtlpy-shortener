from django.conf.urls.defaults import patterns, include, handler500
from django.conf import settings
from django.views.generic.simple import redirect_to
from django.contrib import admin
admin.autodiscover()

handler500 # Pyflakes

urlpatterns = patterns(
    '',
    (r'^admin/(.*)', admin.site.root),
    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    (r'^$', redirect_to, {'url': 'http://montrealpython.org/'}),
    (r'^short/$', 'mtlpy.shortener.views.index'),
    (r'^detail/(\S+)$', 'mtlpy.shortener.views.detail'),
    (r'^json/$', 'mtlpy.shortener.views.json'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )

urlpatterns += patterns('',
                        # This must be last
                        (r'^(\S+)$', 'mtlpy.shortener.views.short'),
                       )
