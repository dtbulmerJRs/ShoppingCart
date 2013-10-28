__author__ = 'Julian Khandros'

from django.contrib import admin
from ShoppingCartApp.models import *

class ProductOrderInline(admin.TabularInline):
    model = ProductOrder
    extra = 10

class OrderAdmin(admin.ModelAdmin):
    inlines = (ProductOrderInline, )

admin.site.register(Product)
admin.site.register(Order, OrderAdmin)
admin.site.register(Store)
admin.site.register(ProductOrder)
admin.site.register(ProductCart)


