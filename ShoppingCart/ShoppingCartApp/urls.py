from django.conf.urls import patterns, url

from ShoppingCartApp import views
from ShoppingCartApp.views import *

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register_user, name='register'),
    url(r'^register_success/$', views.register_success, name='register_success'),
    url(r'^login/$', login_page, name='login_page'),
    url(r'^customer_home/$', CustomerListView.as_view(), name='customer_home'),
    #url(r'^merchant_home/$', MerchantListView, name='merchant_home'),
)