from distutils.archive_util import make_zipfile
from itertools import product
from pyexpat import model
from statistics import mode
from unicodedata import name
from django.db import models

# Create your models here.
# here we are creating a Product class(for database)
# this product class has different columans and we are specifying them
# each field has models.<somthing> - this <> will decide the type of field we want to genereate inside the database

class Promotion(models.Model):
    description = models.CharField(max_length = 255)
    discount = models.FloatField()

#-----------------------------------------------------------------------------------------------------------------------------

class Collection(models.Model):
    titel = models.CharField(max_length = 255)

#-----------------------------------------------------------------------------------------------------------------------------

class Product(models.Model):
    titel = models.CharField(max_length = 255) #varchar-255
    description = models.TextField()
    price = models.DecimalField(max_digits = 6, decimal_places = 2) #9999.99
    inventory = models.IntegerField()
    last_update = models.DateField(auto_now_add = True)

    collection = models.ForeignKey(Collection, on_delete = models.PROTECT)
    promotions = models.ManyToManyField(Promotion)

#------------------------------------------------------------------------------------------------------------------------------

PAYMENT_PENDING = 'P'
PAYMENT_COMPLETED = 'C'
PAYMENT_FAILED = 'F'

PAYMENT_STATUS_CHOICES = [
    (PAYMENT_PENDING,'Pending'),
    (PAYMENT_COMPLETED,'Complete'),
    (PAYMENT_FAILED,'Failed')
]
class Order(models.Model):
    placed_at = models.DateTimeField(auto_now_add = True)
    payment_status = models.CharField(max_length = 1,choices = PAYMENT_STATUS_CHOICES, default = PAYMENT_PENDING)
    
    product = models.ForeignKey(Product, on_delete = models.PROTECT)

#------------------------------------------------------------------------------------------------------------------------------

MEMBERSHIP_BRONZE = 'B'
MEMBERSHIP_SILVER = 'S'
MEMBERSHIP_GOLD = 'G'

MEMBERSHIP_CHOICE = [
    (MEMBERSHIP_BRONZE, 'Bronze'),
    (MEMBERSHIP_SILVER, 'Silver'),
    (MEMBERSHIP_GOLD, 'Gold')
]
class Customer(models.Model):
    first_name = models.CharField(max_length = 300)
    last_name = models.CharField(max_length = 300)
    email = models.EmailField(unique = True)
    phone = models.CharField(max_length = 300)
    birth_date = models.DateField(null = True)
    membership = models.CharField(max_length = 1, choices = MEMBERSHIP_CHOICE, default = MEMBERSHIP_BRONZE)
    
    order = models.ForeignKey(Order, on_delete = models.CASCADE)

#---------------------------------------------------------------------------------------------------------------------------------

class Address(models.Model):
    street = models.CharField(max_length = 255)
    city = models.CharField(max_length = 255)
    # setting up the relation, here parent class is customer
    # also we are setting on_delete which will delete the address if parent entry gets deleted.
   
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)

#--------------------------------------------------------------------------------------------------------------------------------

class Cart(models.Model):
    count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)


#--------------------------------------------------------------------------------------------------------------------------------
class Items(models.Model):
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits = 6, decimal_places = 2)

    cart = models.ForeignKey(Cart, on_delete = models.CASCADE)
    order = models.ForeignKey(Order, on_delete = models.CASCADE)
    Product = models.ForeignKey(Product, on_delete = models.CASCADE)
