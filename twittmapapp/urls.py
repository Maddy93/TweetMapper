from django.conf.urls import patterns, url

from twittmapapp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<category>(\w+))/$', views.tweets_category, name='detail')
)