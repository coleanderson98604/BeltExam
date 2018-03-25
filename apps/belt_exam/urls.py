from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^/add$',views.add),
    url(r'^/create$',views.create),
    url(r'^/(?P<id>\d+)/show',views.show),
    url(r'^/logout',views.logout),
    url(r'^/(?P<id>\d+)/join',views.join)

]
