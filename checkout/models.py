from django.db import models
from project4.settings import AUTH_USER_MODEL
from products.models import Product
from django.utils import timezone
from decimal import Decimal
from datetime import timedelta, datetime

# Create your models here.


class Charge(models.Model):
    full_name = models.CharField(max_length=50, blank=False)
    phone_number = models.CharField(max_length=8, blank=False)
    country = models.CharField(max_length=40, blank=False)
    postcode = models.CharField(max_length=6, blank=True)
    town_or_city = models.CharField(max_length=40, blank=False)
    street_address1 = models.CharField(max_length=40, blank=False)
    street_address2 = models.CharField(max_length=40, blank=True)
    date = models.DateField()

    def __str__(self):
        return "{0}-{1}-{2}".format(self.id, self.date, self.full_name)


class Transaction(models.Model):

    status_options = [
        ('pending', "Pending"),
        ('approved', "Approved"),
        ('rejected', "Rejected"),
        ('shipping', "Shipping"),
        ('delivered', "Delivered"),
        ('lost', "Lost")

    ]

    charge = models.ForeignKey('Charge', on_delete=models.CASCADE, null=True)
    status = models.CharField(
        blank=False,
        choices=status_options,
        max_length=50)
    date = models.DateField()
    owner = models.ForeignKey(
        "accounts.MyUser",
        on_delete=models.SET_NULL,
        null=True)

    def __str__(self):
        return str(self.id)


class LineItem(models.Model):
    product = models.ForeignKey(
        'products.product',
        null=True,
        on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=False)
    price = models.IntegerField(blank=False)
    transaction = models.ForeignKey('Transaction', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def cost(self):
        return self.price * self.quantity
