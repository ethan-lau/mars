#!/usr/bin/python
# -*- coding: utf-8 -*-

# author: liuhanlong
# date: 16/8/17 下午11:41
from rest_framework import serializers
from crawl.models import Crawl, PageReference, LANGUAGE_CHOICES, STYLE_CHOICES


class CrawlSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Crawl.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

    class Meta:
        model = Crawl
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style')


class PageReferenceSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    file = serializers.CharField(required=True)
    url_md5 = serializers.CharField(required=True)
    url = serializers.CharField(required=True)
    source = serializers.CharField(required=True)
    author = serializers.CharField(required=True)
    update_time = serializers.DateTimeField(required=True)

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = PageReference
        fields = ('id', 'title', 'url', 'source', 'author', 'update_time')


