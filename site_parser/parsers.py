import re
from tags.models import WebsiteTag, Tag
from .models import Word


class WebsiteParserMeta(type):
    parsers = []

    def __new__(mcs, name, bases, dct):
        parser = type.__new__(mcs, name, bases, dct)
        mcs.parsers.append(parser)
        return parser

    @classmethod
    def parse_all(mcs, website_data):
        for parser in mcs.parsers:
            try:
                parser().parse(website_data)
            except NotImplementedError:
                pass


class AbstractWebsiteParser(object):
    __metaclass__ = WebsiteParserMeta

    def parse(self, website_data):
        raise NotImplementedError('Called abstract parser!')


class WordParser(AbstractWebsiteParser):
    def parse(self, website_data):
        for word in Word.objects.all():
            if (word.case_sensitive and word.word in website_data.html) or (not word.case_sensitive and word.word.lower() in website_data.html.lower()):
                WebsiteTag.objects.create(website=website_data.website, tag=word.tag)


class ImageParser(AbstractWebsiteParser):
    IMAGE_THRESHOLD = 3
    TAG_TITLE = 'images'

    def parse(self, website_data):
        if len(re.findall(r'<img.*?>', website_data.html, re.DOTALL | re.IGNORECASE)) > self.IMAGE_THRESHOLD:
            try:
                tag = Tag.objects.get(title=self.TAG_TITLE)
                WebsiteTag.objects.create(website=website_data.website, tag=tag)
            except WebsiteTag.DoesNotExist:
                pass
