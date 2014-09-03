from django.conf.urls import patterns, url


urlpatterns = patterns('crawler.views',
    url(r'^start/crawl/$', 'crawl_start', name='crawl_start'),
)
