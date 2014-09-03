from django.contrib import admin
from .models import Website, WebsiteSnapshot
from tags.models import Tag, WebsiteTag


class WebsiteAdmin(admin.ModelAdmin):
    list_display = ['url', 'added', 'is_active', 'snapshots_created', 'website_tags', 'to_be_crawled']
    search_fields = ['url']
    readonly_fields = ['to_be_crawled']
    list_filter = ['is_active']
    change_list_template = 'admin/change_website_list.html'

    def snapshots_created(self, obj):
        return '<a href="/crawler/websitesnapshot/?q=%s">%s</a>' % (obj.url, obj.snapshots.count())
    snapshots_created.allow_tags = True

    def website_tags(self, obj):
        return '<a href="/tags/websitetag/?q=%s">%s</a>' % (obj.url,
            Tag.objects.filter(pk__in=WebsiteTag.objects.filter(website=obj).values_list('tag__pk')).distinct().count())
    website_tags.allow_tags = True


class WebsiteSnaphotAdmin(admin.ModelAdmin):
    list_display = ['website', 'code', 'added']
    list_filter = ['code']
    search_fields = ['website__url']
    readonly_fields = ['website', 'code', 'html', 'exception']


admin.site.register(Website, WebsiteAdmin)
admin.site.register(WebsiteSnapshot, WebsiteSnaphotAdmin)
