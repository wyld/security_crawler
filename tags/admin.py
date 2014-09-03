from django.contrib import admin
from crawler.models import Website
from .models import Tag, WebsiteTag


class WebsiteTagAdmin(admin.ModelAdmin):
    list_display = ['website', 'tag', 'added']
    search_fields = ['website__url', 'tag__title']
    list_filter = ['tag']
    readonly_fields = ['website', 'tag']


class TagAdmin(admin.ModelAdmin):
    list_display = ['title', 'tagged_websites']

    def tagged_websites(self, obj):
        return '<a href="/tags/websitetag/?tag__id__exact=%s">%s</a>' % (obj.pk,
            Website.objects.filter(pk__in=WebsiteTag.objects.filter(tag=obj).values_list('website__pk')).distinct().count())
    tagged_websites.allow_tags = True


admin.site.register(Tag, TagAdmin)
admin.site.register(WebsiteTag, WebsiteTagAdmin)
