from django.conf.urls import patterns, include, url
from django.contrib import admin
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cloud.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('twittmapapp.urls')),
    url(r'^twittmapapp/', include('twittmapapp.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
