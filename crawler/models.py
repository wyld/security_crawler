from django.db import models


class Website(models.Model):
    url = models.URLField(unique=True)
    is_active = models.BooleanField(default=True)
    to_be_crawled = models.BooleanField(default=False)
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['url']

    def __unicode__(self):
        return self.url


class WebsiteSnapshot(models.Model):
    EXCEPTION_CODE = 'error'

    website = models.ForeignKey('crawler.Website', related_name='snapshots')
    code = models.CharField(max_length=20)
    html = models.TextField()
    exception = models.TextField(blank=True)
    added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Website Snapshot (readonly)'
        verbose_name_plural = 'Website Snapshots (readonly)'
        ordering = ['-added']

    def __unicode__(self):
        return '%s - %s' % (self.website.url, self.added.isoformat(' '))
