from django.conf.urls import url
import views


urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^news/$', views.news, name='news'),
    url(r'^events/$', views.events, name='events'),
    url(r'^results/$', views.results, name='results'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^join/$', views.join, name='join'),
    url(r'^resources/$', views.resources, name='resources'),
    url(r'^(?P<post_id>[\d]+)/(?P<post_slug>[\w\-\d\/]+)/image/$', views.image, name='image'),
    url(r'^(?P<post_id>[\d]+)/(?P<post_slug>[\w\-\d\/]+)/$', views.post, name='post'),
]
