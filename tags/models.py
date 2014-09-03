from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.title


class WebsiteTag(models.Model):
    website = models.ForeignKey('crawler.Website', related_name='tags')
    tag = models.ForeignKey('tags.Tag', related_name='tagged')
    added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '[%s] %s' % (self.tag.title, self.website.url)

    class Meta:
    	verbose_name = 'Website Tag (readonly)'
    	verbose_name_plural = 'Website Tags (readonly)'