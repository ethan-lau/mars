#!/usr/bin/python
# -*- coding: utf-8 -*-

# author: liuhanlong
# date: 16/8/17 下午11:38

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([item[1][0], item[0]] for item in LEXERS)
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Crawl(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)


class PageReference(models.Model):
    title = models.CharField(max_length=1024, blank=False, default='')
    file = models.CharField(max_length=512, blank=True, default='')
    url_md5 = models.CharField(max_length=32, blank=True, default='')
    url = models.CharField(max_length=1024, blank=True, default='')
    source = models.CharField(max_length=512, blank=True, default='')
    author = models.CharField(max_length=128, blank=True, default='')
    update_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-update_time',)
        db_table = 'page_reference'


