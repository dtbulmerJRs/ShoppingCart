from django.conf.urls import patterns, url

from ShoppingCartApp import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register_user),
    url(r'^register_success/$', views.register_success),
)