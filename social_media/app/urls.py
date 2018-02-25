# -*- coding: utf-8 -*-
__author__ = 'adityasharma'
from django.conf.urls import url, patterns
from . import views

# api_urlpatterns = patterns(
#     'social_media.app.views',
#     url(r'^user$', 'user', name='app.user')
# )
urlpatterns = [
    url(r'^user$', views.user, name='user')
]