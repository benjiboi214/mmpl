from django.conf.urls import patterns, url
#from core.views import FeedView
import views

#urlpatterns = patterns('',
#        url(r'^$', views.index, name='index'))

urlpatterns = [
    
    url(r'^$', views.index, name='index'),
    url(r'^news/$', views.news, name='news'),
    url(r'^events/$', views.events, name='events'),
    url(r'^results/$', views.results, name='results'),
    url(r'^(?P<form_context>contact)/$', views.contact, name='contact'),
    url(r'^(?P<form_context>join)/$', views.contact, name='join'),
    url(r'^resources/$', views.resources, name='resources'),
    #url(r'^testing/$', FeedView.as_view()),
    url(r'^(?P<post_name_slug>[\w\-\d\/]+)/$', views.post, name='post'),
]
