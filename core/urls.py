from django.conf.urls import patterns, url
import views

#urlpatterns = patterns('',
#        url(r'^$', views.index, name='index'))

urlpatterns = [
    
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<post_name_slug>[\w\-\d\/]+)/$', views.post, name='post'),
]

