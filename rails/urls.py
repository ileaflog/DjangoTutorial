from django.conf.urls import patterns, url

from rails import views

urlpatterns = patterns('',
    # ex: /rails/
    url(r'^$', views.index, name='index'),
    # ex: /rails/5/
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /rails/5/results/
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /rails/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)