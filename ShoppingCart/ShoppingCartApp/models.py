"""
Groups: Merchant, Customer (will be created using admin)
Users:  Will be created using the "registration" plugin app from yesterday's tutorial experiment, and belong to one of
        groups above

Legend
    -- : 1 to 1
    -< : 1 to many

Model relationships
    Merchant User (inherit from User) -- Store -< Product

    Customer User (inherit from User) -- Cart  -< Product
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


class Merchant(User):

    def store(self):
        Store.objects.get(merchant=self)

    def __str__(self):
        return "%d: %s %s" % (self.id, self.first_name, self.last_name)


class Customer(User):

    def cart(self):
        Cart.objects.get(customer=self)

    def orders(self):
        Order.objects.filter(customer=self)

    def __str__(self):
        return "%d: %s %s" % (self.id, self.first_name, self.last_name)


class Store(models.Model):
    name = models.CharField(max_length=100)
    merchant = models.OneToOneField(Merchant)

    def products(self):   ###  need to test this one
        Product.objects.filter(store=self)

    def __str__(self):
        return "%d: %s which belongs to %s" % (self.id, self.name, self.merchant)


class Order(models.Model):
    customer = models.ForeignKey(Customer)

    def products(self):
        Product.objects.filter(order=self)

    def total(self):
        tot = 0
        for product in Product.objects.filter(order=self):
            tot += product.price
        return tot

    def __str__(self):
        return "%s" % self.customer


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    store = models.ForeignKey(Store)
    orders = models.ManyToManyField(Order)

    def __str__(self):
        return "%s which costs %d and belongs to %s" % (self.name, self.price, self.store)


class Cart(models.Model):
    customer = models.OneToOneField(Customer)
    products = models.OneToManyField(Product)

    def total(self):
        tot = 0
        for product in Product.objects.filter(order=self):
            tot += product.price
        return tot

    def __str__(self):
        return "Cart for %s" % self.customer
