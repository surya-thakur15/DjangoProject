from django.conf.urls import url, include
# for views we need to import views from current directory.
from django.urls import path

from . import views

urlpatterns = [
    # /music/
    url(r'^$', views.index, name='index'),

    # music/id
    url(r'^(?P<album_id>[0-9]+)/$', views.detial, name='detail'),
]
