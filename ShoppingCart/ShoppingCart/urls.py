from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http.response import HttpResponseRedirect


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ShoppingCart.views.home', name='home'),
    # url(r'^ShoppingCart/', include('ShoppingCart.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ShoppingCartApp/', include('ShoppingCartApp.urls', namespace="ShoppingCartApp")),

    (r'^$', lambda r : HttpResponseRedirect('ShoppingCartApp/')),
)
