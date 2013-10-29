"""
Groups: Merchant, Customer (will be created using admin)
Users:  Will be created using the "registration" plugin app from yesterday's tutorial experiment, and belong to one of
        groups above

Legend
    -- : 1 to 1
    -< : 1 to many

Model relationships
    Merchant -- Store -< Product

    Customer -- Cart  -< Product
             -- Order -< Product

Model outline
    Store: name, Merchant, Products
    Product: name, price, Store (maybe should also include qty and decrement for every order)
    Cart: Customer, Product/qty dictionary, total
    Order: Product, total

Rules
    Merchant User only sees own store
    Customer User only sees own carts and orders
"""

from django.db import models
from django.contrib.auth.models import User


class Store(models.Model):
    name = models.CharField(max_length=100)
    merchant = models.OneToOneField(User)

    def products(self):
        return Product.objects.filter(store=self)

    def __str__(self):
        return "%d: %s which belongs to %s" % (self.id, self.name, self.merchant)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    store = models.ForeignKey(Store)

    def __str__(self):
        return "%d: %s which costs %d and belongs to %s" % (self.id, self.name, self.price, self.store)


class Cart(models.Model):
    customer = models.OneToOneField(User)
    products = models.ManyToManyField(Product, through='ProductCart')

    def get_products(self):
        product_results = set()
        product_carts = ProductCart.objects.filter(cart=self)
        for product_cart in product_carts:
            product_results.add(product_cart.product)
        return product_results

    def total(self):
        tot = 0
        for product in self.products():
            tot += product.price
        return tot

    def __str__(self):
        return "%d: Cart for %s" % (self.id, self.customer)


class ProductCart(models.Model):
    product = models.ForeignKey(Product)
    cart = models.ForeignKey(Cart)


class Order(models.Model):
    customer = models.ForeignKey(User)
    products = models.ManyToManyField(Product, through='ProductOrder')

    def total(self):
        tot = 0
        for product in self.products():
            tot += product.price
        return tot

    def __str__(self):
        return "%d: %s" % (self.id, self.customer)


class ProductOrder(models.Model):
    product = models.ForeignKey(Product)
    order = models.ForeignKey(Order)






