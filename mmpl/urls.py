from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings


urlpatterns = [
    # Examples:
    # url(r'^$', 'mmpl.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('core.urls')),
    url(r'^search/', include('haystack.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]
