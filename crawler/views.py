from subprocess import Popen
from django.contrib import messages
from django.shortcuts import redirect
from .models import Website


def crawl_start(request):
    Website.objects.filter(is_active=True).update(to_be_crawled=True)
    Popen('python manage.py make_snapshots', shell=True)
    messages.success(request, 'Started website crawling job. Please check website tags once "to be crawled" flag is removed from website.')
    return redirect(request.META.get('HTTP_REFERER', '/'))
