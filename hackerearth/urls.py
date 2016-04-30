from __future__ import absolute_import
from django.conf.urls import url
from .views import CodeView, CodeDetailView


urlpatterns = [
    url(r'^code/$', CodeView.as_view()),
    url(r'^code/(\d*)/$', CodeDetailView.as_view()),
    ]
