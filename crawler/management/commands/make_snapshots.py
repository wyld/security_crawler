import sys
import requests
from requests.exceptions import RequestException
from django.core.management.base import BaseCommand
from crawler.models import Website, WebsiteSnapshot
from site_parser.parsers import WebsiteParserMeta


class Command(BaseCommand):
    help = 'Makes snapshots for all active websites in admin'
    args = ""
    
    def handle(self, *args, **options):
        if len(args) > 0:
            sys.stderr.write("This command requires no arguments.\n")
            return

        for website in Website.objects.filter(is_active=True):
            try:
                response = requests.get(website.url)
                website_data = WebsiteSnapshot.objects.create(website=website, code=response.status_code, html=response.text)
                print 'Got %s snapshot' % website.url

                WebsiteParserMeta.parse_all(website_data)
            except RequestException, e:
                WebsiteSnapshot.objects.create(website=website,
                                               code=WebsiteSnapshot.EXCEPTION_CODE,
                                               html=WebsiteSnapshot.EXCEPTION_CODE,
                                               exception=unicode(e))
                print 'Got error for %s website: %s' % (website.url, unicode(e))
            finally:
                website.to_be_crawled = False
                website.save()
        print 'Finished'
