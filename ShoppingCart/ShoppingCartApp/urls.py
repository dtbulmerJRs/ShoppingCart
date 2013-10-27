from django.conf.urls import patterns, url

from ShoppingCartApp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)