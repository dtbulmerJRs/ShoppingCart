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
        return Order.objects.filter(customer=self)

    def __str__(self):
        return "%d: %s %s" % (self.id, self.first_name, self.last_name)


class Store(models.Model):
    name = models.CharField(max_length=100)
    merchant = models.OneToOneField(Merchant)

    def products(self):
        return Product.objects.filter(store=self)

    def __str__(self):
        return "%d: %s which belongs to %s" % (self.id, self.name, self.merchant)


class Cart(models.Model):
    customer = models.OneToOneField(Customer)

    def products(self):
        return Product.objects.filter(carts=self)

    def total(self):
        tot = 0
        for product in self.products():
            tot += product.price
        return tot

    def __str__(self):
        return "%d: Cart for %s" % (self.id, self.customer)


class Order(models.Model):
    customer = models.ForeignKey(Customer)

    def products(self):
        return Product.objects.filter(orders=self)

    def total(self):
        tot = 0
        for product in self.products():
            tot += product.price
        return tot

    def __str__(self):
        return "%d: %s" % (self.id, self.customer)


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    store = models.ForeignKey(Store)
    orders = models.ManyToManyField(Order)
    carts = models.ManyToManyField(Cart)

    def __str__(self):
        return "%d: %s which costs %d and belongs to %s" % (self.id, self.name, self.price, self.store)



