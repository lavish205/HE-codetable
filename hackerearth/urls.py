from __future__ import absolute_import
from django.conf.urls import url
from .views import CodeView


urlpatterns = [
    url(r'^$', CodeView.as_view()),

    ]