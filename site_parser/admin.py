from django.contrib import admin
from .models import Word


class WordAdmin(admin.ModelAdmin):
    list_display = ['word', 'tag', 'case_sensitive']
    search_fields = ['word', 'tag']
    list_filter = ['case_sensitive']


admin.site.register(Word, WordAdmin)
