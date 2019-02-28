# !/usr/bin/env python

from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    url('^$', views.index, name='index'),
    url('^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]