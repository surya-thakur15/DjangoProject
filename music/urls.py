from django.conf.urls import url, include
# for views we need to import views from current directory.
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
