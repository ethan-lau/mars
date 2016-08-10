#!/usr/bin/python
# coding=utf8
# author: liuhanlong
# date: 16/8/10 下午10:45
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
]
